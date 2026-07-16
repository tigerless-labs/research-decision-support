# Publish the committed canvas on GitHub Pages

The committed canvas is fully self-contained — Pages only has to serve it, never rebuild
it. The canvas path below is never guessed: read it from the `"canvas"` key in
`.design-harness/config.json` (missing key → ask the human with option pickers). Then
**check where it sits** — at the repo root or under `docs/`, both routes below work;
anywhere else, only the Actions route works, because deploy-from-branch serves nothing
but `/` and `/docs`.

**Deploy from branch (zero workflow; canvas at `/` or under `docs/` only).** Enable
once — ask the human, or run it yourself with their approval:

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
