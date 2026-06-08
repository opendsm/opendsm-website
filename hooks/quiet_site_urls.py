"""Silence the per-replacement INFO logging from the mkdocs-site-urls plugin."""

import logging


def on_config(config, **kwargs):
    logging.getLogger("mkdocs.plugins.mkdocs_site_urls").setLevel(logging.WARNING)

    return config
