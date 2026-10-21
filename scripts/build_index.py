import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "posts"

META_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
FIELD_RE = re.compile(r"^(title|date|category|summary|subject):\s*(.+)$", re.MULTILINE)

def parse_meta(text, filename):
    match = META_RE.match(text)
    if not match:
        raise ValueError(f"{filename} 缺少元信息块（文件开头应有 --- 包裹的 title/date/category）")
    fields = dict(FIELD_RE.findall(match.group(1)))
    for key in ("title", "date", "category"):
        if key not in fields:
            raise ValueError(f"{filename} 缺少字段: {key}")
    return fields

def main():
    entries = []
    for md in sorted(POSTS.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        meta = parse_meta(text, md.name)
        entry = {
            "file": md.name,
            "title": meta["title"].strip(),
            "date": meta["date"].strip(),
            "category": meta["category"].strip(),
            "summary": meta.get("summary", "").strip(),
        }
        if "subject" in meta:
            entry["subject"] = meta["subject"].strip()
        entries.append(entry)
    entries.sort(key=lambda e: e["date"], reverse=True)
    out = POSTS / "post.json"
    out.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"生成 {out.name}: {len(entries)} 篇文章")

if __name__ == "__main__":
    main()
