"""Principal Module."""

import logging
from pathlib import Path
from typing import Final

import pytz
from tomli import load

__author__ = '@britodfbr'
__version__ = ''
TITLE: Final[str] = 'incolume-py-sorteio-xlsx'
TZ: Final = pytz.timezone('America/Sao_Paulo')

try:
    configfile = Path(__file__).parents[3].joinpath('pyproject.toml')
    versionfile = Path(__file__).parent.joinpath('version.txt')

    with configfile.open('rb') as file:
        versionfile.write_text(
            f"{load(file)['tool']['poetry']['version']}\n",
            encoding='utf-8',
        )
    __version__ = versionfile.read_text(encoding='utf-8').strip()
except (FileNotFoundError, FileExistsError) as err:
    logging.warning(err)


if __name__ == '__main__':
    logging.debug('%s, %s', configfile, versionfile)
    logging.debug('Vesion load: %s', __version__)
