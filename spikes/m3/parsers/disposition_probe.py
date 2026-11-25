"""Research-only reconciliation contract, not a Markdown parser or sanitizer."""
from dataclasses import dataclass
import html
from urllib.parse import urlsplit, unquote
import unittest

@dataclass(frozen=True)
class Span:
    start: int
    end: int
    disposition: str
    reason: str = ""

def reconcile(raw, spans):
    """Require contiguous UTF-8 coverage and explicit disposition; never infer semantics."""
    cursor = 0
    errors = []
    for span in spans:
        if span.start != cursor or not span.start < span.end <= len(raw):
            errors.append("invalid coverage")
            return errors
        try:
            raw[span.start:span.end].decode("utf-8")
        except UnicodeDecodeError:
            errors.append("split UTF-8 character")
        if span.disposition not in {"preserved", "transformed", "manual", "unsupported"}:
            errors.append("unaccounted span")
        elif span.disposition != "preserved" and not span.reason.strip():
            errors.append("missing explanation")
        if span.disposition == "unsupported":
            errors.append("unsupported span blocks conversion")
        cursor = span.end
    if cursor != len(raw):
        errors.append("incomplete coverage")
    return errors

def candidate_link(value):
    """Conservative experiment: inspect decoded aliases, not browser URL semantics."""
    decoded = html.unescape(value)
    try:
        decoded = unquote(decoded, errors="strict")
        if any(ord(c) <= 32 or ord(c) == 127 for c in decoded):
            return False
        if "\\" in decoded or "%" in decoded or "&" in decoded:
            return False
        p = urlsplit(decoded)
        return (p.scheme.lower() in {"https", "http"} and bool(p.hostname)
                and p.username is None and p.password is None)
    except (ValueError, UnicodeError):
        return False

class Tests(unittest.TestCase):
    def test_complete(self):
        raw = "café\n[ref]: https://example.com/\n".encode()
        split = len("café\n".encode())
        self.assertEqual(reconcile(raw, [Span(0,split,"preserved"),
            Span(split,len(raw),"transformed","reference definition resolved")]), [])

    def test_missing_and_overlap(self):
        for spans in ([Span(0,1,"preserved")], [Span(0,1,"preserved"),Span(0,3,"preserved")],
                      [Span(1,3,"preserved")]):
            self.assertTrue(reconcile(b"abc", spans))

    def test_unaccounted(self):
        self.assertIn("unaccounted span", reconcile(b"x",[Span(0,1,"unknown")]))

    def test_explanation(self):
        self.assertIn("missing explanation", reconcile(b"x",[Span(0,1,"transformed")]))

    def test_unsupported(self):
        self.assertIn("unsupported span blocks conversion",
            reconcile(b"x",[Span(0,1,"unsupported","raw construct")]))

    def test_utf8_boundary(self):
        self.assertIn("split UTF-8 character",
            reconcile("é".encode(),[Span(0,1,"preserved"),Span(1,2,"preserved")]))

    def test_encoded_targets(self):
        for target in ("javascript:alert(1)", "java&#x73;cript:x", "%6aavascript:x",
                       "java%0ascript:x", "java&#9;script:x", "data:text/html,x",
                       "//example.com", "https://user@example.com", "https://example.com\\x",
                       " https://example.com", "https://example.com/%250a"):
            with self.subTest(target=target):
                self.assertFalse(candidate_link(target))
        self.assertTrue(candidate_link("https://example.com/path"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
