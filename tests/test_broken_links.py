import sys

from sphinx_testing import with_app
try:
    from StringIO import StringIO  # Python 2
except ImportError:
    from io import StringIO  # Python 3


# Currently not working as I'm not able to get the complete console output of a sphinx build.

@with_app(buildername='html', srcdir='doc_test/broken_links')
def test_doc_build_html(app, status, warning):
    backup = sys.stdout
    sys.stderr = StringIO()

    app.build()
    sys.stderr.flush()
    out = sys.stderr.getvalue()
    sys.stdout.close()  # close the stream
    sys.stdout = backup  # restore original stdout

    # assert "Needs: linked need" in out