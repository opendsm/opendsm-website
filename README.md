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
- [Mkdocs-Macros](https://mkdocs-macros-plugin.readthedocs.io/en/latest/)
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

### Versioning

The published site is versioned with [mike](https://github.com/jimporter/mike). Each
documentation version is `major.minor` and mirrors an opendsm release; patch releases
(`vX.Y.Z`) refresh the existing `X.Y` version rather than creating a new one. The root of
the site redirects to the `latest` alias.

Deployment is automated in `.github/workflows/website_deployment.yaml`:

- Pushing to `main` publishes the `dev` version.
- Pushing a `vX.Y.Z` tag publishes/refreshes version `X.Y`, moves the `latest` alias to it,
  and sets it as the default.
- The `workflow_dispatch` trigger (Actions → Run workflow) publishes an arbitrary version,
  used to **backfill prior versions**: check out a branch containing the content for that
  version, then run the workflow with the desired `version` (e.g. `1.1`) and optional `alias`.

To preview versions locally, use `mike serve` instead of `mkdocs serve`. To deploy a version
by hand (writes to the `gh-pages` branch):
```python
. .venv/bin/activate
mike deploy --push --update-aliases 1.2 latest   # publish version 1.2 and move `latest`
mike set-default --push latest                   # root redirects to `latest`
mike list                                         # show published versions
```
