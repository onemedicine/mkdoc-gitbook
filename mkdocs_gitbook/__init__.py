# coding: utf-8

from __future__ import absolute_import, unicode_literals

import os
from mkdocs import utils
from mkdocs.plugins import BasePlugin

class GitBookPlugin(BasePlugin):
    """ Default theme for GitBook for Mkdocs. """

    def on_pre_build(self, config, **kwargs):
        "Generate page JSON for site directory."
        project_dir = os.getcwd()

