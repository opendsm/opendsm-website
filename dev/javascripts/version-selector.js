// Relocate the mike version selector to the right of the header bar, directly
// left of the light/dark palette toggle. Material injects `.md-version` into
// the site-title topic (left side) at runtime, so this waits for the injection
// and moves it out to a direct child of the header, where the title's
// flex-grow pushes it to the far right. It also switches the list from
// open-on-hover to open-on-click.
(function () {
  function wireClickToOpen(version) {
    const current = version.querySelector(".md-version__current");

    if (!current || current.dataset.clickToggle) {
      return;
    }

    current.dataset.clickToggle = "true";

    current.addEventListener("click", function (event) {
      event.stopPropagation();
      version.classList.toggle("md-version--open");
    });

    document.addEventListener("click", function (event) {
      if (!version.contains(event.target)) {
        version.classList.remove("md-version--open");
      }
    });
  }

  function relocate() {
    const version = document.querySelector(".md-version");
    const inner = document.querySelector(".md-header__inner");

    if (!version || !inner) {
      return false;
    }

    if (version.parentElement !== inner) {
      const palette = inner.querySelector(".md-header__option");

      if (palette) {
        inner.insertBefore(version, palette);
      } else {
        inner.appendChild(version);
      }
    }

    wireClickToOpen(version);

    return true;
  }

  if (relocate()) {
    return;
  }

  const observer = new MutationObserver(function () {
    if (relocate()) {
      observer.disconnect();
    }
  });

  observer.observe(document.body, { childList: true, subtree: true });
})();
