"""Synthetic-only safety and reconciliation probe, not a production DOCX validator."""
import io, zipfile, re, unittest
from collections import Counter
from urllib.parse import urlsplit, unquote
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
R = "{http://schemas.openxmlformats.org/package/2006/relationships}"
LIMIT = 65536

def package(parts):
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_STORED) as z:
        for name, data in parts:
            z.writestr(name, data)
    return out.getvalue()

def preflight(data):
    if len(data) > 4 * LIMIT:
        raise ValueError("archive size")
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        seen = set()
        total = 0
        for info in z.infolist():
            name = info.filename
            if name in seen or name.startswith("/") or "\\" in name or ":" in name or ".." in name.split("/"):
                raise ValueError("unsafe or duplicate path")
            seen.add(name)
            total += info.file_size
            if info.file_size > LIMIT or total > 4 * LIMIT or len(seen) > 64:
                raise ValueError("resource limit")
        roots = {}
        for info in z.infolist():
            if info.filename.endswith((".xml", ".rels")):
                raw = z.read(info)
                # Deliberately restrict spike fixtures to UTF-8, reject DTD and entities.
                s = raw.decode("utf-8")
                if "\x00" in s or re.search(r"<!\s*(DOCTYPE|ENTITY)", s, re.I):
                    raise ValueError("unsafe XML")
                roots[info.filename] = ET.fromstring(s)
        if "word/document.xml" not in roots:
            raise ValueError("missing body")
        return roots

def inventory(roots):
    root = roots["word/document.xml"]
    records = []
    def walk(node, path):
        tag = node.tag.removeprefix(W)
        if tag in {"t", "delText"}:
            records.append((path, tag, node.text or ""))
        if tag in {"hyperlink", "ins", "del", "txbxContent", "tbl", "gridSpan", "vMerge"}:
            records.append((path, tag, ""))
        for i, child in enumerate(node):
            walk(child, path + "/" + str(i))
    walk(root, "")
    external = [x.get("Target") for name, tree in roots.items() if name.endswith(".rels")
                for x in tree.iter(R+"Relationship") if x.get("TargetMode") == "External"]
    return records, external

def reconcile(expected, actual):
    return list((Counter(expected)-Counter(actual)).elements()), list((Counter(actual)-Counter(expected)).elements())

def safe_link(value):
    decoded = unquote(value).strip()
    if any(ord(c) < 32 or ord(c) == 127 for c in decoded):
        return False
    try:
        p = urlsplit(decoded)
        return p.scheme.lower() in {"http", "https"} and bool(p.hostname) and not p.username and not p.password
    except ValueError:
        return False

XML = f'<w:document xmlns:w="{W[1:-1]}"><w:body><w:p><w:r><w:t>Start</w:t></w:r><w:hyperlink><w:r><w:t>Link</w:t></w:r></w:hyperlink><w:ins><w:r><w:t>Added</w:t></w:r></w:ins><w:del><w:r><w:delText>Deleted</w:delText></w:r></w:del><w:r><w:txbxContent><w:p><w:r><w:t>Box</w:t></w:r></w:p></w:txbxContent></w:r></w:p><w:tbl><w:tr><w:tc><w:tcPr><w:gridSpan w:val="2"/></w:tcPr><w:p><w:r><w:t>Merged</w:t></w:r></w:p><w:tbl><w:tr><w:tc><w:p><w:r><w:t>Nested</w:t></w:r></w:p></w:tc></w:tr></w:tbl></w:tc></w:tr></w:tbl></w:body></w:document>'
RELS = f'<Relationships xmlns="{R[1:-1]}"><Relationship Id="r1" TargetMode="External" Target="https://example.com/image.png" Type="synthetic"/></Relationships>'
def fixture():
    return package([("word/document.xml", XML), ("word/_rels/document.xml.rels", RELS)])

class Tests(unittest.TestCase):
    def test_complex_inventory(self):
        rows,_=inventory(preflight(fixture()))
        self.assertEqual([v for _,t,v in rows if t in {"t","delText"}], ["Start","Link","Added","Deleted","Box","Merged","Nested"])
        self.assertEqual(sum(t=="tbl" for _,t,_ in rows),2)
        self.assertTrue({"hyperlink","ins","del","txbxContent","gridSpan"} <= {t for _,t,_ in rows})
    def test_reconciliation(self):
        rows,_=inventory(preflight(fixture()))
        self.assertEqual(reconcile(rows,rows),([],[]))
        missing,extra=reconcile(rows,rows[1:]+[rows[-1],(rows[0][0],rows[0][1],"changed")])
        self.assertEqual(len(missing),1); self.assertEqual(len(extra),2)
    def test_external(self):
        self.assertEqual(inventory(preflight(fixture()))[1],["https://example.com/image.png"])
    def test_urls(self):
        for bad in ["javascript:alert(1)","%6aavascript:alert(1)","data:text/html,x","file:///tmp/a","//example.com","https://user@example.com","java\nscript:alert(1)"]:
            self.assertFalse(safe_link(bad),bad)
        self.assertTrue(safe_link("https://example.com"))
    def test_invalid_zip(self):
        with self.assertRaises(zipfile.BadZipFile): preflight(b"bad")
    def test_bad_xml(self):
        with self.assertRaises(ET.ParseError): preflight(package([("word/document.xml","<broken>")]))
    def test_dtd(self):
        with self.assertRaises(ValueError): preflight(package([("word/document.xml","<!DOCTYPE a><a/>")]))
    def test_path(self):
        data = package([("word/document.xml", XML), ("../escape", "x")])
        with self.assertRaisesRegex(ValueError, "unsafe or duplicate path"): preflight(data)
    def test_duplicate(self):
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore",UserWarning)
            data=package([("word/document.xml",XML),("word/document.xml",XML)])
        with self.assertRaises(ValueError): preflight(data)
    def test_size(self):
        with self.assertRaises(ValueError): preflight(package([("word/document.xml",b"x"*(LIMIT+1))]))
    def test_missing_body(self):
        with self.assertRaises(ValueError): preflight(package([("other.xml","<a/>")]))

if __name__ == "__main__":
    unittest.main(verbosity=2)
