The website wis made using the following:
- mkdocs: https://www.mkdocs.org/
- mkdocstrings: https://mkdocstrings.github.io/
- mkdocs material theme: https://squidfunk.github.io/mkdocs-material/
- pymdown-extensions: https://facelessuser.github.io/pymdown-extensions/
- mkdocs-section-index: https://oprypin.github.io/mkdocs-section-index/
- mkdocs-site-urls: https://octoprint.github.io/mkdocs-site-urls/

Automatic code documentations assumes google-style docstrings. 
For examples on how to format google-style docstrings, see here: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

### To install
On a Mac with Apple Silicon it may be necessary to first install some relevant libraries that are needed for OpenDSM:
```
brew install openblas
brew install lapack
```
Each of the above will also prompt you to set some environment variables with commands like `export LDFLAGS="/some/appropriate/location/"`, so run these commands one at a time and look at the tail end of the output for instruction.

Run
```python
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m mkdocs serve
```

### To run
From docs folder run:
```python
. .venv/bin/activate
python3 -m mkdocs serve
```