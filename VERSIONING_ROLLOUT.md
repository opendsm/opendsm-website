# Documentation versioning rollout

This site uses [mike](https://github.com/jimporter/mike) to publish versioned docs.
The machinery is in place on the `add-versioning` branch; this document explains how to
take it live and how to operate it afterward. Delete this file once the site is live and
the steps below are part of normal practice.

## Versioning model

- A documentation version is `major.minor` (e.g. `1.2`) and mirrors an opendsm release.
- Patch releases (`vX.Y.Z`) **refresh** the existing `X.Y` version; `Z` never gets its own version.
- `main` publishes a `dev` version. The newest stable release carries the `latest` alias.
- The site root redirects to `latest`.
- mike sorts `versions.json` on every write: `dev` on top, then releases newest→oldest.
  Backfilled older versions slot into the right place automatically — deploy order does not matter.

## What is already done

- `mike` dependency + `version.provider: mike` / `default: latest` in `mkdocs.yml`.
- Deploy workflow `.github/workflows/website_deployment.yaml`:
  - push to `main`/`master` → `mike deploy --push dev`
  - push tag `vX.Y.Z` → `mike deploy --push X.Y latest` + `mike set-default --push latest`
  - `workflow_dispatch` (Actions → Run workflow) → publish an arbitrary version (for backfilling)
- Version selector relocated to the header right (left of the palette toggle), opens on click,
  styled like the search bar (`src/javascripts/version-selector.js`, `src/css/custom.css`).
- A local-only `src/versions.json` preview stub is gitignored (mike generates the real one on `gh-pages`).

## Previewing locally

The version selector only renders when a `versions.json` is reachable, so plain `mkdocs serve`
needs the stub:

```bash
python3 -m venv .venv && . .venv/bin/activate
python3 -m pip install .
cat > src/versions.json <<'JSON'
[
  {"version": "dev", "title": "dev", "aliases": []},
  {"version": "1.2", "title": "1.2", "aliases": ["latest"]},
  {"version": "1.1", "title": "1.1", "aliases": []}
]
JSON
mkdocs serve -a localhost:8001 -w ..
```

The stub's first entry is shown as "current" under `mkdocs serve` (there is no version path to match);
the real site shows the version of the page you are on. To preview the true multi-version experience,
use `mike serve` after a local `mike deploy` (slower — each version is a full build).

## Going live (one time)

The current `gh-pages` branch holds a flat, unversioned site. Pushing to `main` alone only adds a
`/dev/` build and leaves the old site at the root, so finish the migration deliberately.

1. **Record the rollback point** (the live `gh-pages` tip), in case a deploy looks wrong:
   ```bash
   git fetch origin gh-pages
   git rev-parse origin/gh-pages    # save this SHA; was 29ef8ee at rollout authoring
   ```
   To restore: `git push origin <saved-sha>:gh-pages --force`.

2. **Merge `add-versioning` to `main`.** CI publishes the `dev` version. The root is still the old
   flat site at this point.

3. **Publish the first stable version and set the default.** Any one of:
   - Push a tag to **this** repo: `git tag v1.2.7 && git push origin v1.2.7` (CI deploys `1.2`,
     sets `latest`, redirects the root). Use the current opendsm release number.
   - Actions → Run workflow with `version=1.2`, `alias=latest`, `set_default=true`.
   - Locally: `mike deploy --push 1.2 latest && mike set-default --push latest`.

4. **Clean up stale flat files** (optional but recommended). After migration the old top-level
   directories (`assets/`, `documentation/`, `caltrack/`, `community/`, …) linger at the `gh-pages`
   root. New visitors are fine (root redirects), but old deep links like `/documentation/...` would
   resolve to stale copies. Remove them while **keeping `CNAME`**:
   ```bash
   git fetch origin gh-pages && git checkout gh-pages
   git rm -r --quiet assets caltrack community css documentation install javascripts overrides \
     search 404.html index.html objects.inv sitemap.xml sitemap.xml.gz
   git checkout origin/gh-pages -- CNAME   # ensure custom domain is preserved
   # leave the mike-managed version dirs, versions.json, and the redirect index.html in place
   git commit -m "Remove pre-mike flat site from gh-pages root" && git push origin gh-pages
   ```
   Verify `opendsm.energy` redirects to `/1.2/` and the custom domain still resolves.

## Recurring operations

| Event | Action |
|---|---|
| New `main` content | None — `dev` rebuilds automatically on push |
| New stable docs version | Push a `vX.Y.Z` tag to **this** repo (or Run workflow with that `X.Y`). CI publishes `X.Y`, moves `latest`, redirects root. |
| Backfill an older version | Run workflow with the target `version` (see below) |

### Backfilling an older version

1. Create a branch whose content reflects that version (edit prose/methodology as needed).
2. For accurate auto-generated API docs, pin opendsm to that release in `pyproject.toml` on the
   branch (`opendsm @ git+https://github.com/opendsm/opendsm@vX.Y.Z`); otherwise mkdocstrings
   documents `master`.
3. Actions → Run workflow, selecting that branch as the ref, with `version=X.Y` (leave `alias` blank
   and `set_default` unchecked unless it should become the newest stable).

## Gotchas

- **Tags live on this repo, not opendsm.** Releasing opendsm does not auto-publish a docs version;
  tag this repo (or Run workflow) per docs version.
- **`CNAME` must stay at the `gh-pages` root** for the custom domain. mike preserves existing root
  files, but any manual `gh-pages` cleanup must keep it.
- **Backfilled API docs follow the pinned opendsm**, not the version label — pin in `pyproject.toml`
  on the backfill branch.
- **Always use `site:`-prefixed links for internal pages and assets** (e.g. `site:assets/...`,
  `site:community/...`), never root-absolute `/assets/...`. The `mkdocs_site_urls` plugin rewrites
  `site:` to the active version's base (`/X.Y/...`); root-absolute links bypass it and break once the
  site is served under a version path.
