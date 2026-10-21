"""Tests for VORLI release preflight behavior."""
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestReleasePreflight(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(
            [sys.executable, "agent/build.py"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

    def test_current_draft_is_blocked_for_known_release_gaps(self):
        from agent.release_preflight import release_blockers
        blockers = release_blockers()
        self.assertIn("Identità del titolare/responsabile non compilata.", blockers)
        self.assertIn("Contatto ufficiale non compilato.", blockers)
        self.assertIn("Pagina privacy ancora preliminare: serve revisione prima del lancio.", blockers)
        self.assertIn("Nessuna offerta verificata e approvata pronta per la pubblicazione.", blockers)
        self.assertIn("Il catalogo contiene ancora almeno una scheda dimostrativa.", blockers)
        self.assertIn("Le pagine sono in noindex: prima del lancio va decisa e verificata la strategia di indicizzazione.", blockers)
        self.assertIn("Le impostazioni GitHub Pages (branch/cartella di pubblicazione) richiedono una verifica manuale: il controllo automatico non può confermarle.", blockers)

    def test_preflight_does_not_claim_publication_or_compliance(self):
        from agent.release_preflight import release_blockers
        self.assertTrue(release_blockers(), "The current draft must not be treated as release-ready")


if __name__ == "__main__":
    unittest.main()
