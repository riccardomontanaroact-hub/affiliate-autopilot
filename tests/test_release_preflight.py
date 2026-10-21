"""Tests for VORLI release preflight behavior."""
import unittest
from agent.release_preflight import release_blockers


class TestReleasePreflight(unittest.TestCase):
    def test_current_draft_is_blocked_for_known_release_gaps(self):
        blockers = release_blockers()
        joined = "\n".join(blockers)
        self.assertIn("Identità del titolare/responsabile non compilata.", blockers)
        self.assertIn("Contatto ufficiale non compilato.", blockers)
        self.assertIn("Pagina privacy ancora preliminare: serve revisione prima del lancio.", blockers)
        self.assertIn("Nessuna offerta verificata e approvata pronta per la pubblicazione.", blockers)
        self.assertIn("Il catalogo contiene ancora almeno una scheda dimostrativa.", blockers)

    def test_preflight_does_not_claim_publication_or_compliance(self):
        blockers = release_blockers()
        self.assertTrue(blockers, "The current draft must not be treated as release-ready")


if __name__ == "__main__":
    unittest.main()
