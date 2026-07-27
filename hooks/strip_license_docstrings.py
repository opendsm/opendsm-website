# Griffe extension that removes Apache license boilerplate from docstrings before
# mkdocstrings renders them. Older opendsm releases (pinned on version/X.Y branches)
# carry the license header as a module docstring rather than a comment, which would
# otherwise render as the module description on API pages.
import re

from griffe import Extension



_LICENSE = re.compile(
    r"\s*Copyright \d{4}(?:-\d{4})? OpenDSM contributors.*?"
    r"limitations under the License\.?\s*",
    re.DOTALL,
)


class StripLicenseDocstrings(Extension):
    def on_instance(self, *, obj, **kwargs):
        docstring = getattr(obj, "docstring", None)
        if docstring is None:
            return

        cleaned = _LICENSE.sub("", docstring.value)
        if cleaned == docstring.value:
            return

        if cleaned.strip():
            docstring.value = cleaned.strip()
        else:
            obj.docstring = None
