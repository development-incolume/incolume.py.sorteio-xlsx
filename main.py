"""Main module."""

# ruff: noqa: ERA001
import flet

from incolume.py.sorteio_xlsx.gui import ft
# from incolume.py.sorteio_xlsx.gui import tratativas as t1
# from incolume.py.sorteio_xlsx.gui import psg

if __name__ == '__main__':
    # flet.app(t1.tratativa3)
    flet.app(ft.interface_gui)
    # psg.interface_gui()
