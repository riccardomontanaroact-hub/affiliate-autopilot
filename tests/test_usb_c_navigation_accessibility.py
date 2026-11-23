from html.parser import HTMLParser
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
PAGE = REPO_ROOT / "preview" / "vorli-next" / "usb-c.html"


class NavigationParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.nav_depth = 0
        self.navs = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "nav":
            self.nav_depth += 1
            self.navs.append(attributes)
        elif tag == "a" and self.nav_depth:
            self.links.append(attributes)

    def handle_endtag(self, tag):
        if tag == "nav" and self.nav_depth:
            self.nav_depth -= 1


class UsbCNavigationAccessibilityTests(unittest.TestCase):
    def test_navigation_has_accessible_name_and_current_section(self):
        parser = NavigationParser()
        parser.feed(PAGE.read_text(encoding="utf-8"))
        parser.close()

        self.assertEqual(len(parser.navs), 1, "La pagina deve avere una sola navigazione principale")
        self.assertEqual(
            parser.navs[0].get("aria-label"),
            "Navigazione principale",
            "La navigazione deve avere un nome accessibile",
        )

        current_links = [
            link for link in parser.links
            if link.get("aria-current") == "page"
        ]
        self.assertEqual(len(current_links), 1, "Deve esserci un solo link corrente")
        self.assertEqual(
            current_links[0].get("href"),
            "risorse.html",
            "La pagina USB-C appartiene alla sezione Risorse",
        )


if __name__ == "__main__":
    unittest.main()
