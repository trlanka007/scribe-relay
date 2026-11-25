"""Bounded synthetic OPC relationship experiment; no network or extraction."""
import posixpath
import unittest
from urllib.parse import urlsplit, unquote
from xml.etree import ElementTree as ET

REL = "{http://schemas.openxmlformats.org/package/2006/relationships}"
REF = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"

def relationship_source(name):
    if name == "_rels/.rels":
        return ""
    folder, filename = posixpath.split(name)
    if posixpath.basename(folder) != "_rels" or not filename.endswith(".rels"):
        raise ValueError("invalid relationship part")
    return posixpath.join(posixpath.dirname(folder), filename[:-5])

def resolve(source, target, mode, parts):
    if mode == "External":
        return ("external", target)  # report only; never fetch
    if mode not in (None, "Internal"):
        return ("invalid", target)
    if target.startswith((" ", "//")) or any(ord(c) < 32 or ord(c) == 127 for c in target):
        return ("invalid", target)
    try:
        u = urlsplit(target)
        if "%2f" in u.path.lower():
            return ("invalid", target)
        path = unquote(u.path, errors="strict")
    except (ValueError, UnicodeError):
        return ("invalid", target)
    if (u.scheme or u.netloc or u.query or u.fragment or not path
            or "\\" in path or "%" in path or ":" in path
            or any(ord(c) < 32 or ord(c) == 127 for c in path)):
        return ("invalid", target)
    path_segments = path.split("/")
    if path.startswith("/"):
        path_segments = path_segments[1:]
    if any(not segment for segment in path_segments) or path_segments[-1] in (".", ".."):
        return ("invalid", target)
    segments = [] if path.startswith("/") else posixpath.dirname(source).split("/")
    segments = [s for s in segments if s]
    for segment in path.split("/"):
        if segment in ("", "."):
            continue
        if segment == "..":
            if not segments:
                return ("invalid", target)
            segments.pop()
        else:
            segments.append(segment)
    normalized = "/".join(segments)
    return ("resolved" if normalized in parts else "missing", normalized)

def graph(parts):
    """Input is trusted, bounded synthetic part names and already parsed XML."""
    edges = {}
    for name, tree in parts.items():
        if not name.endswith(".rels"):
            continue
        source = relationship_source(name)
        if source and source not in parts:
            raise ValueError("missing relationship source")
        if tree.tag != REL + "Relationships":
            raise ValueError("invalid relationship root")
        for node in tree.findall(REL + "Relationship"):
            rid, target, kind = (node.get(k) for k in ("Id", "Target", "Type"))
            if not rid or not target or not kind or (source, rid) in edges:
                raise ValueError("invalid or duplicate relationship")
            state, resolved = resolve(source, target, node.get("TargetMode"), parts)
            edges[source, rid] = (kind, state, resolved)
    return edges

def references(source, tree, edges):
    """Ordered occurrence records; repeated references are separate occurrences."""
    rows = []
    def visit(node, path):
        for attr, rid in node.attrib.items():
            if attr in {REF+"id", REF+"embed", REF+"link"}:
                rows.append((source, path, attr, rid, edges.get((source, rid))))
        for i, child in enumerate(node):
            visit(child, path + (i,))
    visit(tree, ())
    return rows

def rels(*entries):
    root = ET.Element(REL+"Relationships")
    for rid, target, mode in entries:
        attrs = {"Id":rid, "Target":target, "Type":"synthetic"}
        if mode is not None:
            attrs["TargetMode"] = mode
        ET.SubElement(root, REL+"Relationship", attrs)
    return root

def fixture():
    doc = ET.Element("body")
    for rid in ("rId1", "rId1", "rId2", "rId3", "rId9"):
        ET.SubElement(doc, "drawing", {REF+"embed":rid})
    header = ET.Element("header", {REF+"id":"rId1"})
    return {
        "_rels/.rels":rels(("rId1","word/document.xml",None)),
        "word/document.xml":doc,
        "word/header1.xml":header,
        "word/media/image1.png":None,
        "word/_rels/document.xml.rels":rels(
            ("rId1","media/image1.png",None),
            ("rId2","media/missing.png",None),
            ("rId3","https://example.com/image.png","External")),
        "word/_rels/header1.xml.rels":rels(("rId1","document.xml",None)),
    }

class Tests(unittest.TestCase):
    def test_root(self):
        self.assertEqual(graph(fixture())["","rId1"][1:], ("resolved","word/document.xml"))
    def test_scoped_ids(self):
        e=graph(fixture())
        self.assertNotEqual(e["word/document.xml","rId1"],e["word/header1.xml","rId1"])
    def test_occurrences(self):
        p=fixture(); rows=references("word/document.xml",p["word/document.xml"],graph(p))
        self.assertEqual([r[1] for r in rows],[(0,),(1,),(2,),(3,),(4,)])
        self.assertEqual(rows[0][4],rows[1][4])
        self.assertEqual([r[4][1] if r[4] else "unbound" for r in rows],["resolved","resolved","missing","external","unbound"])
    def test_relative_and_absolute(self):
        p=fixture()
        self.assertEqual(resolve("word/sub/a.xml","../media/image1.png",None,p),("resolved","word/media/image1.png"))
        self.assertEqual(resolve("word/sub/a.xml","/word/media/image1.png",None,p),("resolved","word/media/image1.png"))
    def test_invalid_targets(self):
        for target in ("../../escape","%2e%2e/%2e%2e/escape","//host/a","https://host/a","a%5cb","a%00b","a%252fb","a?query","a#fragment"):
            with self.subTest(target=target):
                self.assertEqual(resolve("word/document.xml",target,None,fixture())[0],"invalid")
    def test_raw_and_encoded_controls(self):
        for control in ("\t", "\n", "\r", "\x00", "\x7f", "%09", "%0a", "%0d", "%00", "%7f"):
            target = "media/im" + control + "age1.png"
            with self.subTest(target=target):
                self.assertEqual(resolve("word/document.xml", target, None, fixture()), ("invalid", target))
    def test_malformed_target_aliases(self):
        for target in ("///word/media/image1.png", "//word/media/image1.png", " media/image1.png", "media%2Fimage1.png", "media%2fimage1.png", "media/image1.png/", "media//image1.png", "media/image1.png/.", "media/image1.png/%2e", "media/image1.png/.."):
            with self.subTest(target=target):
                self.assertEqual(resolve("word/document.xml", target, None, fixture()), ("invalid", target))
    def test_duplicate(self):
        p=fixture(); p["word/_rels/document.xml.rels"]=rels(("rId1","a",None),("rId1","b",None))
        with self.assertRaisesRegex(ValueError,"duplicate"): graph(p)
    def test_orphan_relationship_part(self):
        p=fixture(); p["word/_rels/orphan.xml.rels"]=rels(("rId1","a",None))
        with self.assertRaisesRegex(ValueError,"missing relationship source"): graph(p)
    def test_unknown_mode(self):
        self.assertEqual(resolve("word/document.xml","a","Unexpected",fixture())[0],"invalid")
    def test_cycle_is_finite(self):
        p=fixture()
        p["word/_rels/document.xml.rels"]=rels(("rId1","header1.xml",None))
        e=graph(p)
        self.assertEqual(e["word/document.xml","rId1"][2],"word/header1.xml")
        self.assertEqual(e["word/header1.xml","rId1"][2],"word/document.xml")

if __name__ == "__main__":
    unittest.main(verbosity=2)
