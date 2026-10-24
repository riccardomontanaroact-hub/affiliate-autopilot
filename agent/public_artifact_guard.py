"""Fail-closed validation of the static files staged for public GitHub Pages.

This check inspects only the output directory, never source configuration.
Do not print offending paths: filenames may themselves contain private data.
"""
from pathlib import Path
import sys

FORBIDDEN_NAMES = {
    "dashboard.html", "config.json", "credentials.json",
    "secrets.json", "service-account.json",
}
FORBIDDEN_SUFFIXES = {".pem", ".key", ".p12", ".sqlite", ".db"}
FORBIDDEN_DIRS = {".git", ".github", "__pycache__", ".venv"}


def find_unsafe_paths(site: Path) -> list[Path]:
    """Return paths that must never enter a public Pages artifact."""
    site = Path(site)
    if not site.is_dir() or site.is_symlink():
        return [site]

    violations = []
    for path in site.rglob("*"):
        parts = tuple(part.lower() for part in path.relative_to(site).parts)
        name = parts[-1]
        if (
            path.is_symlink()
            or name in FORBIDDEN_NAMES
            or name == ".env"
            or name.startswith(".env.")
            or Path(name).suffix in FORBIDDEN_SUFFIXES
            or any(part in FORBIDDEN_DIRS for part in parts)
        ):
            violations.append(path)
    return violations


def main() -> int:
    if len(sys.argv) != 2:
        print("Expected one Pages output directory", file=sys.stderr)
        return 2
    site = Path(sys.argv[1])
    if not site.is_dir() or site.is_symlink():
        print("Public site directory missing or unsafe", file=sys.stderr)
        return 1
    violations = find_unsafe_paths(site)
    if violations:
        print(f"Blocked {len(violations)} unsafe path(s) in Pages artifact", file=sys.stderr)
        return 1
    print("Pages artifact privacy guard passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
