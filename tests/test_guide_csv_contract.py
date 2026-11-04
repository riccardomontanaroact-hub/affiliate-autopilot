"""Regressioni editoriali offline per guida e scheda CSV VORLI Lab.

Esecuzione: python -m unittest tests/test_guide_csv_contract.py -v
Nessuna richiesta di rete, dipendenza esterna o modifica alla produzione.
"""
import csv
import io
import unittest
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "preview" / "vorli-next"
CATEGORIES = {
    "computer": "Computer",
    "software": "Software",
    "elettronica": "Elettronica",
    "elettrodomestici-smart": "Elettrodomestici smart",
    "accessori-casa": "Accessori casa",
    "sport-tech": "Sport tech",
    "benessere-tech": "Benessere tech",
    "energia-portatile": "Energia portatile",
}
HEADERS = ["categoria", "criterio_da_verificare", "opzione_A",
           "opzione_B", "fonte_ufficiale", "note"]


class GuideParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.article = None
        self.in_li = False
        self.li_parts = []
        self.criteria = {}
        self.links = []
        self.robots = []
        self.ids = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "article" and attrs.get("id") in CATEGORIES:
            self.article = attrs["id"]
            self.criteria[self.article] = []
        if tag == "li" and self.article:
            self.in_li = True
            self.li_parts = []
        if tag == "a":
            self.links.append(attrs.get("href", ""))
        if tag == "meta" and attrs.get("name") == "robots":
            self.robots.append(attrs.get("content", "").lower())

    def handle_data(self, data):
        if self.in_li:
            self.li_parts.append(data)

    def handle_endtag(self, tag):
        if tag == "li" and self.in_li:
            self.criteria[self.article].append(" ".join(
                "".join(self.li_parts).split()))
            self.in_li = False
        if tag == "article":
            self.article = None


class GuideCsvContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.guide = (LAB / "guida-scelta-tech-lab.html").read_text(encoding="utf-8")
        cls.parser = GuideParser()
        cls.parser.feed(cls.guide)
        with (LAB / "scheda-confronto-tech-lab.csv").open(
            encoding="utf-8-sig", newline=""
        ) as stream:
            reader = csv.DictReader(stream)
            cls.headers = reader.fieldnames
            cls.rows = list(reader)

    def test_eight_categories_three_criteria_each(self):
        self.assertEqual(set(self.parser.criteria), set(CATEGORIES))
        for key, items in self.parser.criteria.items():
            with self.subTest(category=key):
                self.assertEqual(len(items), 3)
                self.assertTrue(all(items))

    def test_csv_matches_guide_verbatim(self):
        self.assertEqual(self.headers, HEADERS)
        self.assertEqual(len(self.rows), 24)
        expected = Counter(
            (label, criterion)
            for key, label in CATEGORIES.items()
            for criterion in self.parser.criteria[key]
        )
        actual = Counter((row["categoria"], row["criterio_da_verificare"])
                         for row in self.rows)
        self.assertEqual(actual, expected)

    def test_template_has_no_offers_or_formulas(self):
        for row in self.rows:
            for column in ("opzione_A", "opzione_B", "fonte_ufficiale", "note"):
                self.assertEqual(row[column], "")
            for value in row.values():
                self.assertFalse(value.lstrip().startswith(("=", "+", "-", "@")))

    def test_preview_is_noindex_and_links_resolve(self):
        self.assertIn("noindex", " ".join(self.parser.robots))
        self.assertIn("scheda-confronto-tech-lab.csv", self.parser.links)
        self.assertEqual(len(self.parser.ids), len(set(self.parser.ids)))
        for href in self.parser.links:
            if not href or href.startswith(("http:", "https:", "mailto:", "tel:")):
                continue
            path, _, fragment = href.partition("#")
            if path:
                self.assertTrue((LAB / path).is_file(), href)
            if fragment and not path:
                self.assertIn(fragment, self.parser.ids, href)


if __name__ == "__main__":
    unittest.main()
