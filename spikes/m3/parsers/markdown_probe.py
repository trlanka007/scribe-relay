"""Disposable F10 probe: exact source ledger and parser observations, not a renderer."""
import hashlib
import unittest
from markdown_it import MarkdownIt
import mistune

CASES = {
    'reference': '[Label][ref]\n\n[ref]: https://example.com/\n',
    'unsafe': '[Label](javascript:alert%281%29)\n',
    'encoded': '[Label](java&#x73;cript:alert%281%29)\n',
    'malformed': '[Unclosed](https://example.com/\n',
    'html': '<span>Visible text</span>\n',
    'image': '![Alt](missing.png)\n',
    'unicode': '# తెలుగు café\r\n\r\nText\n',
    'fence': '```text\n[Literal](javascript:x)\n',
}


def probe(source):
    tokens = MarkdownIt('commonmark', {'html': True}).enable('table').parse(source)
    nodes = mistune.create_markdown(renderer='ast', plugins=['table'])(source)
    def walk_tokens(items):
        for t in items:
            yield t
            yield from walk_tokens(t.children or [])
    def walk_nodes(items):
        for n in items:
            yield n
            yield from walk_nodes(n.get('children', []))
    flat = list(walk_tokens(tokens))
    ast = list(walk_nodes(nodes))
    # Physical source lines, not semantic spans; preserve CRLF and Unicode bytes.
    ledger = []
    offset = 0
    for line in source.splitlines(keepends=True):
        end = offset + len(line.encode('utf-8'))
        ledger.append((offset, end, line))
        offset = end
    return {
        'sha256': hashlib.sha256(source.encode('utf-8')).hexdigest(),
        'ledger': ledger,
        'markdown_links': [t.attrs.get('href') for t in flat if t.type == 'link_open'],
        'mistune_links': [n.get('attrs', {}).get('url') for n in ast if n['type'] == 'link'],
        'markdown_types': [t.type for t in flat],
        'mistune_types': [n['type'] for n in ast],
        'block_maps': [t.map for t in tokens if t.map is not None],
    }


class Tests(unittest.TestCase):
    def test_exact_source_ledger(self):
        for name, source in CASES.items():
            with self.subTest(name=name):
                result = probe(source)
                raw = source.encode('utf-8')
                cursor = 0
                for start, end, line in result['ledger']:
                    self.assertEqual(start, cursor)
                    self.assertEqual(raw[start:end], line.encode('utf-8'))
                    cursor = end
                self.assertEqual(cursor, len(raw))

    def test_reference_link(self):
        result = probe(CASES['reference'])
        self.assertEqual(result['markdown_links'], ['https://example.com/'])
        self.assertEqual(result['mistune_links'], ['https://example.com/'])

    def test_unsafe_link_difference(self):
        result = probe(CASES['unsafe'])
        self.assertEqual(result['markdown_links'], [])
        self.assertEqual(result['mistune_links'], ['javascript:alert%281%29'])

    def test_malformed(self):
        result = probe(CASES['malformed'])
        self.assertEqual(result['markdown_links'], [])
        self.assertEqual(result['mistune_links'], [])

    def test_html_is_tokenized_not_rendered(self):
        result = probe(CASES['html'])
        self.assertIn('html_inline', result['markdown_types'])
        self.assertIn('inline_html', result['mistune_types'])

    def test_image_and_fence(self):
        self.assertIn('image', probe(CASES['image'])['markdown_types'])
        self.assertIn('image', probe(CASES['image'])['mistune_types'])
        result = probe(CASES['fence'])
        self.assertIn('fence', result['markdown_types'])
        self.assertEqual(result['markdown_links'], [])
        self.assertEqual(result['mistune_links'], [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
