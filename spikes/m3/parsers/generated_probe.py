"""Generated trusted DOCX comparison only; not an untrusted input validator."""
import io
import unittest
import zipfile
from xml.etree import ElementTree as ET
from docx import Document
from docx.shared import Inches
from PIL import Image
from opc_probe import graph, references, REF

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
DOC = 'word/document.xml'
HEADER = 'word/header1.xml'


def fixture():
    doc = Document()
    doc.sections[0].header.paragraphs[0].text = 'Header outside body'
    doc.add_paragraph('Before')
    image = io.BytesIO()
    Image.new('RGB', (32, 16), 'blue').save(image, format='PNG')
    for label in ('First', 'Second'):
        doc.add_paragraph(label)
        image.seek(0)
        doc.add_picture(image, width=Inches(1))
    doc.add_table(rows=1, cols=1).cell(0, 0).text = 'Cell'
    doc.add_paragraph('After')
    out = io.BytesIO()
    doc.save(out)
    return out.getvalue()


def inspect(data):
    # Generated fixture only: earlier synthetic safety limits are not suitable
    # for typical Office templates; do not expose this function to uploads.
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        parts = {n: ET.fromstring(archive.read(n)) if n.endswith(('.xml', '.rels')) else None
                 for n in archive.namelist()}
    edges = graph(parts)
    body = parts[DOC].find(W + 'body')
    xml_blocks = [(b.tag.removeprefix(W), ''.join(t.text or '' for t in b.iter(W + 't')))
                  for b in body if b.tag != W + 'sectPr']
    doc = Document(io.BytesIO(data))
    library_blocks = [('p', b.text) if b.__class__.__name__ == 'Paragraph'
                      else ('tbl', ''.join(c.text for row in b.rows for c in row.cells))
                      for b in doc.iter_inner_content()]
    media = [r for r in references(DOC, parts[DOC], edges) if r[2] == REF + 'embed']
    header = ''.join(t.text or '' for t in parts[HEADER].iter(W + 't'))
    return xml_blocks, library_blocks, media, header, doc


class Tests(unittest.TestCase):
    def setUp(self):
        self.result = inspect(fixture())

    def test_ordered_blocks(self):
        xml, library, _, _, _ = self.result
        expected = [('p', 'Before'), ('p', 'First'), ('p', ''), ('p', 'Second'),
                    ('p', ''), ('tbl', 'Cell'), ('p', 'After')]
        self.assertEqual(xml, expected)
        self.assertEqual(library, expected)

    def test_asset_occurrences(self):
        _, _, media, _, doc = self.result
        self.assertEqual(len(media), 2)
        self.assertEqual(len(doc.inline_shapes), 2)
        self.assertNotEqual(media[0][1], media[1][1])
        self.assertTrue(all(r[4][1] == 'resolved' for r in media))
        self.assertEqual(len({r[4][2] for r in media}), 1)

    def test_header_accounting_boundary(self):
        xml, _, _, header, doc = self.result
        self.assertEqual(header, 'Header outside body')
        self.assertEqual(doc.sections[0].header.paragraphs[0].text, header)
        self.assertNotIn(header, [text for _, text in xml])

    def test_paragraph_only_omits_table(self):
        _, _, _, _, doc = self.result
        self.assertNotIn('Cell', [p.text for p in doc.paragraphs])
        self.assertEqual(doc.tables[0].cell(0, 0).text, 'Cell')


if __name__ == '__main__':
    unittest.main(verbosity=2)
