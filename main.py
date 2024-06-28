"""Main module."""

# ruff: noqa: ERA001
import flet
# from incolume.py.sorteio_xlsx.gui import ft
from incolume.py.sorteio_xlsx.gui import tratativa1 as t1
# from incolume.py.sorteio_xlsx.gui import psg

if __name__ == '__main__':
    flet.app(t1.main)
    # flet.app(ft.interface_gui)
    # psg.interface_gui()
