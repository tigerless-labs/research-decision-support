# Publish the committed canvas on GitHub Pages

The committed canvas is fully self-contained — Pages only has to serve it, never rebuild
it. The canvas path below is never guessed: read it from the `"canvas"` key in
`.design-harness/config.json` (the human chose it at bootstrap; ask if it's missing).

**Deploy from branch (zero workflow).** GitHub serves only `/` (repo root) or `/docs` in
this mode — usable only when the canvas lives in one of them; otherwise take the Actions
path. Enable once — ask the human, or run it yourself with their approval:

```bash
gh api repos/<owner>/<repo>/pages -X POST \
  -f "source[branch]=<default-branch>" -f "source[path]=/docs"
```

The board is live at `https://<owner>.github.io/<repo>/<canvas path within docs/>`.

**GitHub Actions (any canvas location, or the repo already deploys Pages by workflow).**
Copy the committed file into the artifact; the deploy steps stay the stock Pages actions:

```yaml
- uses: actions/checkout@v4
- run: mkdir -p _site && cp <canvas path> _site/index.html
- uses: actions/upload-pages-artifact@v3
  with:
    path: _site
- uses: actions/deploy-pages@v4
```

Either way the served page is byte-identical to the committed projection: a stale page
means a stale commit — rebuild and commit, never patch the HTML.
