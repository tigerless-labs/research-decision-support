# Publish the committed canvas on GitHub Pages

The committed `canvas.html` is fully self-contained — Pages only has to serve it, never
rebuild it. Pick by what the repo already uses:

**Deploy from branch (zero workflow).** Enable once — ask the human, or run it yourself
with their approval:

```bash
gh api repos/<owner>/<repo>/pages -X POST \
  -f "source[branch]=<default-branch>" -f "source[path]=/docs"
```

The board is live at `https://<owner>.github.io/<repo>/canvas.html`.

**GitHub Actions (the repo already deploys Pages by workflow).** Copy the committed file
into the artifact; the deploy steps stay the stock Pages actions:

```yaml
- uses: actions/checkout@v4
- run: mkdir -p _site && cp docs/canvas.html _site/index.html
- uses: actions/upload-pages-artifact@v3
  with:
    path: _site
- uses: actions/deploy-pages@v4
```

Either way the served page is byte-identical to the committed projection: a stale page
means a stale commit — rebuild and commit, never patch the HTML.
