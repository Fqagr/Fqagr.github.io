# 拾光集

纯手写静态博客，托管在 GitHub Pages。文章用 Markdown 写，列表自动生成。

## 发新文章（自动化流程）

1. 在 `posts/` 里新建 `.md` 文件（文件名建议英文/拼音），开头写元信息块：

```
---
title: 文章标题
date: 2026-10-19
category: notes
summary: 一句话摘要，显示在首页 recent 里
---

# 正文从下面开始写...
```

- `category` 只能填 `notes` 或 `reviews`，决定文章出现在哪个分类页
2. 推送到 GitHub：

```bash
git add -A
git commit -m "发布新文章"
git push
```

3. GitHub 会自动扫描所有文章、生成 `posts/post.json`，首页 recent 和对应分类页会自动更新，**不需要手动改任何链接**。

## 添加电子书

1. 把 PDF 放进 `books/` 文件夹（文件名建议英文）。
2. 打开 `library.html`，按注释里的格式添加一张书卡，`href` 指向 `books/文件名.pdf`。

## 注意

- 推送后线上更新有 1-2 分钟延迟，刷新按 `Ctrl + F5`。
- 本地预览 Markdown 文章：在 `blog` 目录地址栏输入 `cmd`，运行 `python -m http.server 8000`，浏览器开 `http://localhost:8000`。
