"""Safety regression checks for the offline VORLI comparison worksheet.

Run from repository root: python -m unittest tests/test_vorli_csv_export_safety.py
No network, external dependencies, or customer data required.
"""
import csv
import io
import unittest
from collections import Counter
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parents[1] / "preview/vorli-next/scheda-confronto-tech-lab.csv"
HEADERS = ["categoria", "criterio_da_verificare", "opzione_A", "opzione_B", "fonte_ufficiale", "note"]
CATEGORIES = {
    "Computer", "Software", "Elettronica", "Elettrodomestici smart",
    "Accessori casa", "Sport tech", "Benessere tech", "Energia portatile",
}
DANGEROUS_PREFIXES = ("=", "+", "-", "@", "\t", "\r", "\n")


class WorksheetSafetyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = CSV_PATH.read_bytes()
        cls.text = raw.decode("utf-8-sig")
        cls.rows = list(csv.reader(io.StringIO(cls.text, newline=""), strict=True))

    def test_shape_and_category_coverage(self):
        self.assertEqual(self.rows[0], HEADERS)
        self.assertEqual(len(self.rows), 25, "24 criteria plus header")
        self.assertTrue(all(len(row) == len(HEADERS) for row in self.rows))
        self.assertEqual(Counter(row[0] for row in self.rows[1:]),
                         Counter({name: 3 for name in CATEGORIES}))

    def test_blank_user_fields_and_unique_criteria(self):
        self.assertEqual(len({(row[0], row[1]) for row in self.rows[1:]}), 24)
        for row in self.rows[1:]:
            self.assertTrue(row[1].strip(), "Criterion cannot be empty")
            self.assertTrue(all(not cell for cell in row[2:]),
                            "User-editable fields must ship blank")

    def test_no_spreadsheet_formula_payloads(self):
        for row in self.rows:
            for cell in row:
                self.assertFalse(cell.lstrip().startswith(DANGEROUS_PREFIXES),
                                 "Potential spreadsheet formula in CSV export")

    def test_no_control_characters_or_bom_in_cells(self):
        for row in self.rows:
            for cell in row:
                self.assertNotIn("\ufeff", cell)
                self.assertFalse(any(ord(ch) < 32 for ch in cell),
                                 "Unexpected control character in cell")


if __name__ == "__main__":
    unittest.main()
