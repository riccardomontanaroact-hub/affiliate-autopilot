"""Regression checks for the VORLI Pages privacy guard."""
import tempfile
import unittest
from pathlib import Path

from agent.public_artifact_guard import find_unsafe_paths


class PublicArtifactGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.site = Path(self.temp.name) / "site"
        self.site.mkdir()

    def add_file(self, name):
        path = self.site / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("test", encoding="utf-8")

    def test_normal_static_files_are_allowed(self):
        self.add_file("index.html")
        self.add_file("assets/style.css")
        self.assertEqual(find_unsafe_paths(self.site), [])

    def test_blocks_internal_dashboard_and_nested_config(self):
        self.add_file("dashboard.html")
        self.add_file("data/config.json")
        self.assertEqual(len(find_unsafe_paths(self.site)), 2)

    def test_blocks_case_variants_and_env_files(self):
        self.add_file("DASHBOARD.HTML")
        self.add_file(".env.production")
        self.add_file("assets/PRIVATE.KEY")
        self.assertEqual(len(find_unsafe_paths(self.site)), 3)

    def test_blocks_internal_directories(self):
        self.add_file(".git/config")
        self.add_file(".github/workflows/deploy.yml")
        self.assertTrue(find_unsafe_paths(self.site))

    def test_blocks_symlinks(self):
        self.add_file("index.html")
        link = self.site / "link.html"
        try:
            link.symlink_to(self.site / "index.html")
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks unavailable")
        self.assertIn(link, find_unsafe_paths(self.site))

    def test_missing_directory_fails_closed(self):
        self.assertTrue(find_unsafe_paths(self.site / "missing"))


if __name__ == "__main__":
    unittest.main()
