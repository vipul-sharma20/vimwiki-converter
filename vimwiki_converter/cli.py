"""
vimwiki-converter

Usage:
  vimwiki-converter run --config-yml=<config-yml>

Options:
  --config-yml=<config-yml>      Path to file with vimwiki-converter configs.
"""
import io
from docopt import docopt

import yaml

from vimwiki_converter import __version__
from vimwiki_converter import convert


def main():
    args = docopt(__doc__, version=__version__)

    if args["run"]:
        config_file = args["--config-yml"]

        convert.run(config_file)

