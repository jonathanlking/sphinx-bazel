try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path

from sphinx_testing import with_app


@with_app(buildername='html', srcdir='doc_test/bazel_target_workspace')  # , warningiserror=True)
def test_bazel_target_workspace(app, status, warning):
    app.build()
    html = Path(app.outdir, 'index.html').read_text()
    assert 'workspace: workspace_target_example'
    assert 'workspace path: /path/to/my/workspace' in html
