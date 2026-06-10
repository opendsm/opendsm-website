window.MathJax = {
    tex: {
        inlineMath: [["\\(", "\\)"]],
        displayMath: [["\\[", "\\]"]],
        processEscapes: true,
        processEnvironments: true
    },
    chtml: {
        scale: 0.9
    },
    options: {
        ignoreHtmlClass: ".*|",
        processHtmlClass: "arithmatex"
    }
};

// MathJax loads async, so on the first emission (and before its bundle is
// ready) startup/output don't exist yet. Bail until MathJax is initialized;
// it auto-typesets the initial page itself, and this re-typesets on each
// later navigation. Throwing here breaks the document$ chain for subscribers
// registered after it.
document$.subscribe(() => {
    if (!window.MathJax || !MathJax.startup || !MathJax.startup.output) {
        return
    }

    MathJax.startup.output.clearCache()
    MathJax.typesetClear()
    MathJax.texReset()
    MathJax.typesetPromise()
})