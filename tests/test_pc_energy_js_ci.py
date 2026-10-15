"""Run the existing JavaScript regression suite through Python unittest discovery.

The repository's validation workflow already executes:
    python -m unittest discover -s tests -v

This bridge makes the 13 Node.js tests part of that existing CI command
without changing workflow permissions or deploying anything.
"""
from pathlib import Path
import shutil
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
JS_TEST = ROOT / "tests" / "test_pc_energy_mobile.cjs"


class JavaScriptCalculatorCITests(unittest.TestCase):
    def test_pc_energy_mobile_node_suite(self):
        node = shutil.which("node")
        self.assertIsNotNone(node, "Node.js must be installed to validate JavaScript")
        self.assertTrue(JS_TEST.is_file(), "Expected JavaScript test suite is missing")

        result = subprocess.run(
            [node, "--test", str(JS_TEST)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=60,
            check=False,
        )
        self.assertEqual(
            result.returncode,
            0,
            "JavaScript regression suite failed:\n" + result.stdout[-12000:],
        )


if __name__ == "__main__":
    unittest.main()
