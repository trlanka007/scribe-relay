"""F09: compare two views of a generated, trusted DOCX. No untrusted input."""
import hashlib
import io
import posixpath
import unittest
import zipfile
from xml.etree import ElementTree as ET

from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.hyperlink import Hyperlink
from PIL import Image

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
P = '{http://schemas.openxmlformats.org/package/2006/relationships}'
URL = 'https://example.com/article'


def fixture():
    doc = Document()
    doc.add_heading('Title', 1)
    p = doc.add_paragraph('Before ')
    link = OxmlElement('w:hyperlink')
    link.set(qn('r:id'), doc.part.relate_to(URL, RT.HYPERLINK, is_external=True))
    run = OxmlElement('w:r')
    text = OxmlElement('w:t')
    text.text = 'reference'
    run.append(text)
    link.append(run)
    p._p.append(link)
    p.add_run(' after')
    t = doc.add_table(rows=1, cols=2)
    t.cell(0, 0).text = 'Left'
    t.cell(0, 1).text = 'Right'
    png = io.BytesIO()
    Image.new('RGB', (8, 8), 'blue').save(png, format='PNG')
    for label in ('First placement', 'Second placement'):
        doc.add_paragraph(label)
        doc.add_picture(io.BytesIO(png.getvalue()))
    doc.add_paragraph('End')
    doc.sections[0].header.paragraphs[0].text = 'Header sentinel'
    out = io.BytesIO()
    doc.save(out)
    return out.getvalue(), hashlib.sha256(png.getvalue()).hexdigest()


def xml_view(data):
    # This fixture is generated above. Do not apply to arbitrary ZIP packages.
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        root = ET.fromstring(z.read('word/document.xml'))
        rels = ET.fromstring(z.read('word/_rels/document.xml.rels'))
        edges = {r.get('Id'): r for r in rels.findall(P + 'Relationship')}
        rows = []
        for block in root.find(W + 'body'):
            if block.tag == W + 'tbl':
                rows.append(('table', tuple(tuple(''.join(t.text or '' for t in c.iter(W+'t')) for c in row.findall(W+'tc')) for row in block.findall(W+'tr'))))
            elif block.tag == W + 'p':
                for item in block:
                    if item.tag == W + 'hyperlink':
                        edge = edges[item.get(R+'id')]
                        assert edge.get('TargetMode') == 'External' and edge.get('Type') == RT.HYPERLINK
                        rows.append(('link', ''.join(t.text or '' for t in item.iter(W+'t')), edge.get('Target')))
                    elif item.tag == W + 'r':
                        for child in item:
                            if child.tag == W+'t':
                                rows.append(('text', child.text or ''))
                            elif child.tag == W+'drawing':
                                for blip in child.iter(A+'blip'):
                                    edge = edges[blip.get(R+'embed')]
                                    assert edge.get('Type') == RT.IMAGE and edge.get('TargetMode') != 'External'
                                    path = posixpath.normpath(posixpath.join('word', edge.get('Target')))
                                    rows.append(('image', hashlib.sha256(z.read(path)).hexdigest()))
        headers = [r for r in edges.values() if r.get('Type') == RT.HEADER]
        assert len(headers) == 1
        header = ET.fromstring(z.read(posixpath.join('word', headers[0].get('Target'))))
        return rows, ''.join(t.text or '' for t in header.iter(W+'t'))


def library_view(data):
    doc = Document(io.BytesIO(data))
    rows = []
    for block in doc.iter_inner_content():
        if isinstance(block, Table):
            rows.append(('table', tuple(tuple(c.text for c in row.cells) for row in block.rows)))
        else:
            for item in block.iter_inner_content():
                if isinstance(item, Hyperlink):
                    rows.append(('link', item.text, item.url))
                else:
                    if item.text:
                        rows.append(('text', item.text))
                    for drawing in item._element.xpath('.//a:blip'):
                        rel = doc.part.rels[drawing.get(qn('r:embed'))]
                        assert not rel.is_external and rel.reltype == RT.IMAGE
                        rows.append(('image', hashlib.sha256(rel.target_part.blob).hexdigest()))
    return rows, doc.sections[0].header.paragraphs[0].text


class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data, sha = fixture()
        cls.expected = [('text','Title'),('text','Before '),('link','reference',URL),('text',' after'),
                        ('table',(('Left','Right'),)),('text','First placement'),('image',sha),
                        ('text','Second placement'),('image',sha),('text','End')]

    def test_independent_expected_inventory(self):
        self.assertEqual(xml_view(self.data)[0], self.expected)
        self.assertEqual(library_view(self.data)[0], self.expected)

    def test_header_not_silently_ignored(self):
        self.assertEqual(xml_view(self.data)[1], 'Header sentinel')
        self.assertEqual(library_view(self.data)[1], 'Header sentinel')

    def test_duplicate_placement_single_asset(self):
        doc = Document(io.BytesIO(self.data))
        self.assertEqual(len(doc.inline_shapes), 2)
        self.assertEqual(sum(r.reltype == RT.IMAGE for r in doc.part.rels.values()), 1)

    def test_order_is_not_multiset_equality(self):
        changed = self.expected.copy()
        changed[5], changed[7] = changed[7], changed[5]
        self.assertCountEqual(changed, self.expected)
        self.assertNotEqual(changed, self.expected)

    def test_paragraph_only_is_incomplete(self):
        doc = Document(io.BytesIO(self.data))
        self.assertNotIn('Left', [p.text for p in doc.paragraphs])
        self.assertIn(('table',(('Left','Right'),)), xml_view(self.data)[0])


if __name__ == '__main__':
    unittest.main(verbosity=2)
