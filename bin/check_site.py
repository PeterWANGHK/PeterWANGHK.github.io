"""Check rendered routes, publication migration, and local asset/link resolution."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

root = Path(sys.argv[1]).resolve()
baseurl = sys.argv[2].rstrip("/")
expected = ["", "publications", "projects", "cv", "news", "teaching", "talks", "awards", "repositories", "contact"]
for route in expected:
    assert (root / route / "index.html").is_file(), f"Missing route: {route}"

publications = (root / "publications/index.html").read_text(encoding="utf-8")
keys = ["wang2026dream", "wang2026safead", "wang2026drift", "zhang2026mavco", "yu2026pipeline", "xiu2026scene", "cai2026nash", "xu2026gamediffusion"]
for key in keys:
    assert f'id="{key}"' in publications, f"Missing publication: {key}"
assert publications.count('class="title"') == 8, "Expected exactly eight publication titles"
for image in ["dream-methodology.jpg", "drift-methodology.png", "mavco-pipeline.png"]:
    assert image in publications, f"Missing publication preview: {image}"
assert "Under second round of review" in publications
assert "Co-first author" in publications
assert "Albert Einstein" not in (root / "cv/index.html").read_text(encoding="utf-8")


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if "href" in attrs:
            self.links.append(attrs["href"])
        if "src" in attrs:
            self.links.append(attrs["src"])
        if "srcset" in attrs:
            self.links.extend(item.strip().split()[0] for item in attrs["srcset"].split(",") if item.strip())


errors = []
for page in root.rglob("*.html"):
    parser = Links()
    parser.feed(page.read_text(encoding="utf-8"))
    for link in parser.links:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        path = unquote(parsed.path)
        if path.startswith("/"):
            if baseurl and not (path == baseurl or path.startswith(baseurl + "/")):
                errors.append(f"{page.relative_to(root)}: missing baseurl in {link}")
                continue
            target = root / path.removeprefix(baseurl).lstrip("/")
        else:
            target = page.parent / path
        if target.is_dir():
            target /= "index.html"
        if not target.exists():
            errors.append(f"{page.relative_to(root)}: unresolved {link}")
            continue
        if parsed.fragment and target.suffix == ".html":
            destination = Links()
            destination.feed(target.read_text(encoding="utf-8"))
            if unquote(parsed.fragment) not in destination.ids:
                errors.append(f"{page.relative_to(root)}: unresolved anchor {link}")

assert not errors, "\n".join(errors)
print(f"Verified {len(expected)} routes, eight publications, three previews, and local links at baseurl {baseurl!r}.")
