"""Convert posts/*.ipynb to markdown so the regular pipeline picks them up."""
from pathlib import Path

from nbconvert import MarkdownExporter

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "posts"

def main():
    exporter = MarkdownExporter()
    count = 0
    for nb in sorted(POSTS.glob("*.ipynb")):
        body, resources = exporter.from_filename(str(nb))
        (POSTS / (nb.stem + ".md")).write_text(body, encoding="utf-8")
        for rel_path, data in (resources.get("outputs") or {}).items():
            out = POSTS / rel_path
            out.parent.mkdir(parents=True, exist_ok=True)
            if isinstance(data, str):
                out.write_text(data, encoding="utf-8")
            else:
                out.write_bytes(data)
        count += 1
    print(f"converted {count} notebooks")

if __name__ == "__main__":
    main()
