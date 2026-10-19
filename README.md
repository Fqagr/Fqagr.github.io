# 拾光集

这是一个纯手写的静态博客，托管在 GitHub Pages 上。

## 怎么发布一篇文章

1. 复制 `posts/_template.html`，改名为你的文章文件名，比如 `my-first-post.html`（建议用英文或拼音，别用中文文件名，避免链接出问题）。
2. 打开这个新文件，修改 `<title>`、日期、标题和正文。
3. 打开对应分类页面（`reviews.html` 或 `notes.html`），在注释标记的地方添加一条文章链接（格式注释里写了）。
4. 打开 `index.html`，在 `recent/` 区块也加一条同样格式的链接。
5. 推送到 GitHub：

```bash
git add -A
git commit -m "发布新文章"
git push
```

## 怎么添加电子书

1. 把 PDF 文件放进 `books/` 文件夹（文件名建议用英文）。
2. 打开 `library.html`，按注释里的格式添加一张书卡，`href` 指向 `books/文件名.pdf`。
3. 推送即可。访客点开书卡就能在浏览器里直接阅读。

## 注意

- 改完任何文件都要走一遍「add → commit → push」才会更新到线上网站。
- 线上更新一般有 1-2 分钟延迟，刷新时按 `Ctrl + F5`。
