"""Pin the install page and badges to the documented opendsm release.

The version, supported Python versions, and (for superseded versions) the
dependency freeze date are derived from the installed opendsm package and PyPI
release metadata, so a deprecated version's site pins itself with no page edits.
Pages opt in by containing one of the placeholder comments below.
"""

import importlib.metadata
import json
import logging
import os
import urllib.request



log = logging.getLogger("mkdocs.plugins.version_pins")

PACKAGE = "opendsm"
PYPI_URL = f"https://pypi.org/pypi/{PACKAGE}/json"

BADGES_PLACEHOLDER = "<!-- opendsm-badges -->"
INSTALL_PLACEHOLDER = "<!-- opendsm-install -->"

# A superseded version freezes its dependencies to the successor's release date.
# Auto-detection picks the next released (major, minor); override here when an
# intermediate line was skipped (e.g. 1.0 -> 1.2 because 1.1 was abandoned).
SUPERSEDED_BY = {
    "1.0": "1.2",
}

_CURRENT_INSTALL = """There are two supported ways to install OpenDSM:

- Install the latest stable release from [PyPI](https://pypi.python.org/pypi/opendsm). This is best for most users.

- Build the package from source at [https://github.com/opendsm/opendsm](https://github.com/opendsm/opendsm). This is best for advanced users and developers."""

_pins = None


def _major_minor(version):
    parts = version.split(".")
    major = int(parts[0])
    minor = 0
    if len(parts) > 1:
        minor = int(parts[1])

    return major, minor


def _python_versions():
    classifiers = importlib.metadata.metadata(PACKAGE).get_all("Classifier") or []
    prefix = "Programming Language :: Python :: "
    versions = []
    for classifier in classifiers:
        if not classifier.startswith(prefix):
            continue

        value = classifier[len(prefix):].strip()
        if "." in value:
            versions.append(value)

    return versions


def _fetch_releases():
    with urllib.request.urlopen(PYPI_URL, timeout=15) as response:
        payload = json.load(response)

    return payload["releases"]


def _release_date(releases, line):
    uploads = []
    for raw_version, files in releases.items():
        if not files:
            continue

        if f"{_major_minor(raw_version)[0]}.{_major_minor(raw_version)[1]}" == line:
            uploads.extend(item["upload_time_iso_8601"] for item in files)

    if not uploads:
        return None

    earliest = min(uploads)

    return earliest[:10]


def _successor_line(releases, current):
    lines = set()
    for raw_version, files in releases.items():
        if not files:
            continue

        if _major_minor(raw_version) > current:
            lines.add(_major_minor(raw_version))

    if not lines:
        return None

    major, minor = min(lines)

    return f"{major}.{minor}"


def _compute_pins():
    version = importlib.metadata.version(PACKAGE)
    current_line = "{}.{}".format(*_major_minor(version))

    pins = {}
    pins["version"] = version
    pins["python_versions"] = _python_versions()
    pins["deprecated"] = False
    pins["freeze_date"] = None

    forced_date = os.environ.get("OPENDSM_FREEZE_DATE")
    if forced_date:
        pins["deprecated"] = True
        pins["freeze_date"] = forced_date

        return pins

    try:
        releases = _fetch_releases()
        successor = SUPERSEDED_BY.get(current_line) or _successor_line(releases, _major_minor(version))
        if successor is not None:
            pins["freeze_date"] = _release_date(releases, successor)
            pins["deprecated"] = pins["freeze_date"] is not None

    except Exception as error:
        log.warning("Could not reach PyPI; rendering install page as current: %s", error)

    return pins


def _render_badges(pins):
    if pins["deprecated"]:
        version = pins["version"]
        pypi_href = f"https://pypi.org/project/{PACKAGE}/{version}/"
        version_src = f"https://img.shields.io/badge/pypi-v{version}-blue.svg"
        python_label = "%20%7C%20".join(pins["python_versions"])
        python_src = f"https://img.shields.io/badge/python-{python_label}-blue.svg"
        python_href = pypi_href

    else:
        pypi_href = "https://pypi.python.org/pypi/opendsm"
        version_src = "https://img.shields.io/pypi/v/opendsm.svg"
        python_href = "https://pypi.org/project/opendsm"
        python_src = "https://img.shields.io/pypi/pyversions/opendsm.svg"

    badges = f"""<p align="center">
    <a href="{pypi_href}" target="_blank">
        <img src="{version_src}" alt="PyPi Version">
    </a>
    <a href="{python_href}" target="_blank">
        <img src="{python_src}" alt="Supported Python versions">
    </a>
    <a href="https://github.com/opendsm/opendsm" target="_blank">
        <img src="https://img.shields.io/github/license/opendsm/opendsm" alt="License">
    </a>
    <a href="https://github.com/ambv/black" target="_blank">
        <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style">
    </a>
</p>"""

    return badges


def _render_install(pins):
    if not pins["deprecated"]:
        return _CURRENT_INSTALL

    version = pins["version"]
    tag = f"v{version}"
    line = "{}.{}".format(*_major_minor(version))
    install = f"""!!! warning "Deprecated — OpenDSM {line}"

    Deprecated releases are provided as-is, without ongoing support or maintenance.

There are two suggested ways to install OpenDSM:

- Install the `{version}` release using [UV](https://pypi.org/project/opendsm/{version}/), resolving dependencies as they stood when this version was supported. This is best for most users.

    ```bash
    uv pip install "opendsm=={version}" --exclude-newer {pins["freeze_date"]}
    ```

- Build the package from source at the [{tag} release tag](https://github.com/opendsm/opendsm/releases/tag/{tag}). This is best for advanced users and developers."""

    return install


def on_config(config, **kwargs):
    global _pins
    _pins = _compute_pins()
    log.info("opendsm install-page pins: %s", _pins)

    return config


def on_page_markdown(markdown, **kwargs):
    if _pins is None:
        return markdown

    if BADGES_PLACEHOLDER in markdown:
        markdown = markdown.replace(BADGES_PLACEHOLDER, _render_badges(_pins))

    if INSTALL_PLACEHOLDER in markdown:
        markdown = markdown.replace(INSTALL_PLACEHOLDER, _render_install(_pins))

    return markdown
