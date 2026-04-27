# -*- coding: utf-8 -*-

# Standard Python libraries
from __future__ import print_function
import os
import sys
from re import (
    search,
    sub,
    findall
)
from json import loads
from pprint import pprint
try:
    from urllib.request import urlopen
except ImportError:  # Python2
    from urllib import urlopen

from IPython.core.magic import (
    Magics,
    magics_class,
    line_cell_magic
)
from IPython.display import (
    HTML,
    Markdown,
    display
)
from IPython import get_ipython


def GET(url):
    pass


@magics_class
class D3Magics(Magics):

    def __init__(self, **kwargs):
        super(D3Magics, self).__init__(**kwargs)
        self.max_id = 0  # Used to ensure that the current group selection is unique.
        self.src = None  # D3 main library source path.
        self.verbose = False   # Print rendered internal javascript at cell execution
                               # Useful for debugging

        self._cdnjs_d3_source_template = "//cdnjs.cloudflare.com/ajax/libs/d3/%s/d3"
        self._cdnjs_api_url = "http://api.cdnjs.com/libraries/d3"

    def _build_output_code(self, cell):
        pass

    @property
    def last_release(self):
        """Obtain last stable D3 release from cdnjs API.
        If is not possible, return last hardcoded release.
        """
        pass

    @property
    def online_releases(self):
        pass

    def show_online_releases(self):
        """Print all releases hosted at d3 cdnjs page."""
        pass

    @property
    def version(self):
        """Returns version actually in use in the current notebook."""
        pass

    @property
    def modules(self):
        """Return a list of D3 modules, used by examples filter."""
        pass

    @line_cell_magic
    def d3(self, line="", cell=None):
        """D3 line and cell magics. Starting point for all commands."""
        pass

    def doc(self, line):
        """Returns D3 general API documentation reference or
        from one D3 module passed as argument."""
        pass


def load_ipython_extension(ipython):
    pass


if __name__ == "__main__":
    load_ipython_extension(get_ipython())
