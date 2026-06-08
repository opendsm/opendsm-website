The website was made using the following:
- [MkDocs](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Material for MkDocs Extensions](https://squidfunk.github.io/mkdocs-material/setup/extensions/)
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)
- [Awesome Nav for MkDocs](https://lukasgeiter.github.io/mkdocs-awesome-nav/)
- [mkdocstrings](https://mkdocstrings.github.io/)
- [mkdocs-autorefs](https://mkdocstrings.github.io/autorefs/)
- [mkdocs-section-index](https://oprypin.github.io/mkdocs-section-index/)
- [MkDocs Site URLs](https://octoprint.github.io/mkdocs-site-urls/)
- [mkdocs-git-revision-date-localized-plugin](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin)
- [mike](https://github.com/jimporter/mike) (documentation versioning)

Automatic code documentations assumes google-style docstrings. 
For examples on how to format google-style docstrings, see here: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

### To install
_Note for Mac Users:_
On a Mac with Apple Silicon it may be necessary to first install some relevant libraries that are needed for OpenDSM:
```
brew install openblas
brew install lapack
```
Each of the above will also prompt you to set some environment variables with commands like `export LDFLAGS="/some/appropriate/location/"`, so run these commands one at a time and look at the tail end of the output for instruction.

To install the necessary packages, run the following from the opendsm-website directory
```python
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install .
python3 -m mkdocs serve
```

### To run
From opendsm-website directory run:
```python
. .venv/bin/activate
python3 -m mkdocs serve
```
When editing opendsm docstrings (which feed the API reference), also watch the package
source so the API pages live-reload: `mkdocs serve -a localhost:8001 -w ..`

### Versioning

The published site is versioned with [mike](https://github.com/jimporter/mike). Each
documentation version is published at `/vX.Y/` (shown as `X.Y` in the version selector) and
mirrors an opendsm release; patch releases
(`vX.Y.Z`) refresh the existing `vX.Y` version rather than creating a new one. `main` builds
the `dev` version; the newest stable release carries the `stable` alias (shown as a badge in
the version selector), and the site root redirects to `stable`. mike orders the version selector itself (`dev` first, then releases
newest→oldest).

Deployment runs from `.github/workflows/website_deployment.yaml`:

- push to `main` → builds/refreshes the `dev` version (opendsm `@master`)
- push a `vX.Y.Z` tag → builds version `vX.Y`, moves `stable`, sets it as default
- Actions → **Run workflow** (`workflow_dispatch`) → builds an arbitrary version (for backfilling)

#### Each stable version pins opendsm to its release

The API reference is generated from the *installed* opendsm, so a version must be built with
`pyproject.toml` pinning opendsm to that release — otherwise it silently documents `master`
(which can differ substantially). To make this reliable, every published stable version lives
on a long-lived **`version/X.Y` branch**: it is `main`'s content with the opendsm dependency
re-pinned to the release commit/tag. `dev` (built from `main`) keeps `@master`.

`main`, `gh-pages`, and `version/**` are protected from deletion by a repository ruleset.
Force-pushes are still allowed, so the refresh below works.

Publishing or refreshing a stable version (e.g. `1.2`):

1. Rebuild the branch from current `main` and re-pin opendsm:
   ```bash
   git checkout main && git pull
   git checkout -B version/1.2
   # in pyproject.toml: opendsm @ git+https://github.com/opendsm/opendsm@<release-commit-or-tag>
   git commit -am "Pin opendsm to the 1.2 release"
   git push -f origin version/1.2
   ```
2. Actions → **Run workflow** on `version/1.2` with `version=v1.2`, `alias=stable`, `set_default=true`.

Backfilling an older version is the same flow on its own `version/X.Y` branch, dispatched with
`version=vX.Y` (leave `alias`/`set_default` unset unless it should become the newest stable).

#### Local preview

Content and code render with plain `mkdocs serve`. The version-selector dropdown only appears
when a `versions.json` is reachable, so to preview it either run `mike serve` (after a local
`mike deploy`), or drop a throwaway gitignored `src/versions.json`:
```json
[{"version": "dev", "title": "dev", "aliases": []}, {"version": "v1.2", "title": "v1.2", "aliases": ["stable"]}]
```

#### Gotchas

- Internal links and assets must use `site:`-prefixed paths (e.g. `site:assets/...`,
  `site:documentation/...`), never root-absolute `/assets/...`. Only `site:` links are rewritten
  to the active version's base; absolute links break once served under a version path.
- `CNAME` and `robots.txt` live at the **`gh-pages` root**, not under `src/` (which would land in
  a version directory). A manual `gh-pages` cleanup must preserve both.
