# -*- coding: utf-8 -*-

import sphinx

from sphinxcontrib.sphinx_bazel.domain.domain import BazelDomain
from sphinxcontrib.sphinx_bazel.autobazel.common import AutobazelCommonDirective

VERSION = '0.1.6'

def setup(app):
    app.add_domain(BazelDomain)
    app.add_directive('autobazel-workspace', AutobazelCommonDirective)
    app.add_directive('autobazel-package', AutobazelCommonDirective)
    app.add_directive('autobazel-target', AutobazelCommonDirective)
    app.add_directive('autobazel-rule', AutobazelCommonDirective)
    app.add_directive('autobazel-macro', AutobazelCommonDirective)
    app.add_directive('autobazel-implementation', AutobazelCommonDirective)
    app.add_directive('autobazel-attribute', AutobazelCommonDirective)

    return {'version': VERSION}  # identifies the version of our extension
