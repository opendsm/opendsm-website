// Material's instant navigation reconciles <head> on each page swap, removing
// any element whose outerHTML isn't in the freshly-fetched page. Osano injects
// its <style>/<link> into <head> at runtime, so those are absent from the
// fetched HTML and get stripped on every navigation — the consent widget loses
// its styling and flashes before Osano re-injects. Re-attach Osano's head
// elements the moment they're removed; MutationObserver callbacks run before
// the browser paints, so the styling never visibly drops.
(function () {
  var head = document.head;
  var pinned = new Set();

  function isOsano(node) {
    if (node.nodeType !== 1) {
      return false;
    }

    var cls = typeof node.className === "string" ? node.className : "";
    var haystack = [node.id, node.getAttribute("href"), node.getAttribute("src"), cls]
      .filter(Boolean)
      .join(" ");

    if (/osano/i.test(haystack)) {
      return true;
    }

    return node.tagName === "STYLE" && /osano/i.test(node.textContent || "");
  }

  Array.prototype.forEach.call(head.children, function (node) {
    if (isOsano(node)) {
      pinned.add(node);
    }
  });

  new MutationObserver(function (mutations) {
    mutations.forEach(function (mutation) {
      mutation.addedNodes.forEach(function (node) {
        if (isOsano(node)) {
          pinned.add(node);
        }
      });

      mutation.removedNodes.forEach(function (node) {
        if (pinned.has(node) && !head.contains(node)) {
          head.appendChild(node);
        }
      });
    });
  }).observe(head, { childList: true });
})();
