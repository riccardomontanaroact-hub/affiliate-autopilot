from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
ROOT = Path(__file__).parent
PAGES = ["index.html", "catalogo.html", "risorse.html", "guida.html", "usb-c.html"]
class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.images = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "href" in attrs: self.hrefs.append(attrs["href"])
        if tag == "img": self.images.append(attrs.get("src", ""))
def test_preview():
    for name in PAGES:
        content = (ROOT / name).read_text(encoding="utf-8")
        assert 'name="viewport"' in content, name
        assert 'noindex,nofollow' in content, name
        assert "<main" in content and "<h1" in content, name
        p = Links(); p.feed(content)
        assert not p.images, f"external imagery not reviewed: {name}"
        for href in p.hrefs:
            parts = urlsplit(href)
            if parts.scheme in ("http", "https"):
                assert parts.netloc == "github.com", (name, href)
            elif href.startswith("#"): continue
            else:
                assert (ROOT / parts.path).is_file(), (name, href)
    print("PASS: pages, local links, noindex, viewport, image policy")
if __name__ == "__main__": test_preview()
