"""Pre-render posts/*.md into posts/html/*.html (math -> KaTeX-ready HTML)."""
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "posts"
OUT = POSTS / "html"

META_RE = __import__("re").compile(r"^---\s*\n(.*?)\n---\s*\n", __import__("re").DOTALL)

def main():
    OUT.mkdir(exist_ok=True)
    count = 0
    for md in sorted(POSTS.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        body = META_RE.sub("", text, count=1)
        html = markdown.markdown(
            body,
            extensions=["extra", "nl2br", "sane_lists", "pymdownx.arithmatex", "pymdownx.tilde"],
            extension_configs={
                "pymdownx.arithmatex": {"generic": True},
            },
        )
        (OUT / (md.stem + ".html")).write_text(html, encoding="utf-8")
        count += 1
    print(f"rendered {count} posts -> {OUT}")

if __name__ == "__main__":
    main()
