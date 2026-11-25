"""Synthetic package integration experiment, not a general DOCX importer."""
import io
import zipfile
import unittest
from xml.etree import ElementTree as ET
from safety_probe import package, preflight, inventory, W
from opc_probe import graph, references, REF, REL

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
CT = "{http://schemas.openxmlformats.org/package/2006/content-types}"
DOC = "word/document.xml"
IMAGE = "word/media/image1.png"
HEADER = "word/header1.xml"
TYPE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/"

def rel_xml(entries):
    root = ET.Element(REL+"Relationships")
    for rid, kind, target, mode in entries:
        attrs = {"Id":rid, "Type":TYPE+kind, "Target":target}
        if mode:
            attrs["TargetMode"] = mode
        ET.SubElement(root, REL+"Relationship", attrs)
    return ET.tostring(root, encoding="utf-8")

def fixture():
    root = ET.Element(W+"document")
    body = ET.SubElement(root, W+"body")
    def para(text):
        p = ET.SubElement(body, W+"p")
        ET.SubElement(ET.SubElement(p,W+"r"),W+"t").text = text
        return p
    para("Before")
    for label in ("First placement", "Second placement"):
        p = para(label)
        drawing = ET.SubElement(ET.SubElement(p,W+"r"),W+"drawing")
        ET.SubElement(drawing,A+"blip",{REF+"embed":"rId1"})
    p = para("Link: ")
    link = ET.SubElement(p,W+"hyperlink",{REF+"id":"rId2"})
    ET.SubElement(ET.SubElement(link,W+"r"),W+"t").text = "Example"
    tbl = ET.SubElement(body,W+"tbl")
    cell = ET.SubElement(ET.SubElement(tbl,W+"tr"),W+"tc")
    ET.SubElement(ET.SubElement(ET.SubElement(cell,W+"p"),W+"r"),W+"t").text = "Cell"
    para("After")
    sect = ET.SubElement(body,W+"sectPr")
    ET.SubElement(sect,W+"headerReference",{REF+"id":"rId3"})
    header = ET.Element(W+"hdr")
    ET.SubElement(ET.SubElement(ET.SubElement(header,W+"p"),W+"r"),W+"t").text = "Header"
    types = ET.Element(CT+"Types")
    for ext, mime in [("rels","application/vnd.openxmlformats-package.relationships+xml"),("xml","application/xml"),("png","image/png")]:
        ET.SubElement(types,CT+"Default",{"Extension":ext,"ContentType":mime})
    for part, kind in [(DOC,"document.main"),(HEADER,"header")]:
        ET.SubElement(types,CT+"Override",{"PartName":"/"+part,"ContentType":"application/vnd.openxmlformats-officedocument.wordprocessingml."+kind+"+xml"})
    return package([
        ("[Content_Types].xml", ET.tostring(types)),
        ("_rels/.rels",rel_xml([("rId1","officeDocument",DOC,None)])),
        (DOC,ET.tostring(root,encoding="utf-8")),
        (HEADER,ET.tostring(header,encoding="utf-8")),
        ("word/_rels/document.xml.rels",rel_xml([
            ("rId1","image","media/image1.png",None),
            ("rId2","hyperlink","https://example.com/","External"),
            ("rId3","header","header1.xml",None)])),
        (IMAGE,b"synthetic placeholder; not decoded or rendered"),
    ])

def inspect(data):
    roots = preflight(data)
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        parts = {name: roots.get(name) for name in z.namelist()}
    edges = graph(parts)
    main = edges.get(("", "rId1"))
    if main is None or main[1:] != ("resolved", DOC):
        raise ValueError("unexpected synthetic main part")
    texts, _ = inventory(roots)
    refs = references(DOC,roots[DOC],edges)
    body = roots[DOC].find(W+"body")
    blocks = [node.tag.removeprefix(W) for node in body]
    return blocks, texts, refs, edges

class Tests(unittest.TestCase):
    def test_order(self):
        blocks,texts,_,_ = inspect(fixture())
        self.assertEqual(blocks,["p","p","p","p","tbl","p","sectPr"])
        self.assertEqual([v for _,t,v in texts if t=="t"],
                         ["Before","First placement","Second placement","Link: ","Example","Cell","After"])
    def test_asset_identity_and_occurrences(self):
        _,_,refs,_ = inspect(fixture())
        media = [r for r in refs if r[2]==REF+"embed"]
        self.assertEqual(len(media),2)
        self.assertNotEqual(media[0][1],media[1][1])
        self.assertEqual({r[4][2] for r in media},{IMAGE})
        self.assertTrue(all(r[4][1]=="resolved" for r in media))
    def test_external_and_header(self):
        _,_,refs,_ = inspect(fixture())
        self.assertEqual([r[4][1:] for r in refs if r[2]==REF+"id"],
                         [("external","https://example.com/"),("resolved",HEADER)])
    def test_missing_asset(self):
        with zipfile.ZipFile(io.BytesIO(fixture())) as z:
            data = package([(n,z.read(n)) for n in z.namelist() if n!=IMAGE])
        _,_,refs,_ = inspect(data)
        self.assertEqual([r[4][1] for r in refs if r[2]==REF+"embed"],["missing","missing"])
    def test_reordering_is_detectable(self):
        original=inspect(fixture())[0]
        with zipfile.ZipFile(io.BytesIO(fixture())) as z:
            parts=[(n,z.read(n)) for n in z.namelist()]
        modified=[]
        for n,data in parts:
            if n==DOC:
                root=ET.fromstring(data); body=root.find(W+"body")
                table=body[4]; body.remove(table); body.insert(0,table)
                data=ET.tostring(root,encoding="utf-8")
            modified.append((n,data))
        self.assertNotEqual(original,inspect(package(modified))[0])

if __name__=="__main__":
    unittest.main(verbosity=2)
