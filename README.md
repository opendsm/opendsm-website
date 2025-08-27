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