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
        self.assertNotIn("Identità del titolare/responsabile non compilata.", blockers)
        self.assertNotIn("Contatto ufficiale non compilato.", blockers)
        self.assertIn("Pagina privacy ancora preliminare: serve revisione prima del lancio.", blockers)
        self.assertIn("Nessuna offerta verificata e approvata pronta per la pubblicazione.", blockers)
        self.assertIn("Il catalogo contiene ancora almeno una scheda dimostrativa.", blockers)
        self.assertIn("Strategia di indicizzazione non approvata esplicitamente.", blockers)
        self.assertIn("Origine GitHub Pages non verificata manualmente.", blockers)

    def test_preflight_cli_fails_closed_while_release_blockers_remain(self):
        result = subprocess.run(
            [sys.executable, "agent/release_preflight.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("VORLI — PRE-FLIGHT: BLOCCATO", result.stdout)
        self.assertIn("Nessuna offerta verificata e approvata pronta per la pubblicazione.", result.stdout)
        self.assertIn("Origine GitHub Pages non verificata manualmente.", result.stdout)


    def test_preflight_does_not_claim_publication_or_compliance(self):
        from agent.release_preflight import release_blockers
        self.assertTrue(release_blockers(), "The current draft must not be treated as release-ready")


    def test_workflow_does_not_enable_pages_automatically(self):
        workflow = (ROOT / ".github" / "workflows" / "build.yml").read_text(encoding="utf-8")
        self.assertIn("enablement: false", workflow)
        self.assertNotIn("enablement: true", workflow)
        self.assertIn("if: github.ref == 'refs/heads/main'", workflow)
        self.assertIn("vars.VORLI_ENABLE_PAGES_DEPLOY == 'true'", workflow)


    def test_local_fragment_targets_exist(self):
        import re
        pages = ("index.html", "risorse.html", "guida.html", "usb-c.html", "privacy.html", "catalogo.html", "dashboard.html")
        for page in pages:
            html = (ROOT / "site" / page).read_text(encoding="utf-8")
            ids = set(re.findall(r"""\bid=["']([^"']+)["']""", html))
            links = re.findall(r"""href=["']([^"']+)["']""", html)
            for target in links:
                if target.startswith(("https://", "http://", "mailto:", "tel:", "javascript:")):
                    continue
                path, separator, fragment = target.partition("#")
                local = path.split("?", 1)[0] if path else page
                if not local:
                    local = page
                if not separator or not fragment:
                    continue
                target_file = ROOT / "site" / local
                with self.subTest(page=page, target=target):
                    self.assertTrue(target_file.is_file(), f"Missing local target file {local}")
                    target_html = target_file.read_text(encoding="utf-8")
                    target_ids = set(re.findall(r"""\bid=["']([^"']+)["']""", target_html))
                    self.assertIn(fragment, target_ids, f"Missing fragment #{fragment} in {local}")


if __name__ == "__main__":
    unittest.main()
