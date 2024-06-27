"""Main module."""
# ruff: noqa: ERA001

from __future__ import annotations
import logging

import PySimpleGUI as sg  # noqa: N813
from incolume.py.sorteio_xlsx.sorteio import sorteio

import flet as ft
from pathlib import Path


import pytz
from typing import Final

TITLE: Final[str] = 'incolume-py-sorteio-xlsx'
TZ: Final = pytz.timezone('America/Sao_Paulo')
filename = ft.Ref[ft.TextField]()
amount = ft.Ref[ft.TextField]()
greetings = ft.Ref[ft.Column]()


def btn_click(e):
    """Event to click button."""
    page = e.page
    if not filename.current.value:
        filename.current.error_text = 'Favor o arquivo Excel "C:/file.xlsx"'
        page.update()
        return

    if not Path(filename.current.value).is_file():
        filename.current.error_text = 'Parece não ser um arquivo válido'
        page.update()
        return

    filename.current.error_text = ''

    if not amount.current.value:
        amount.current.error_text = 'Favor entre com a quantidade'
        page.update()
        return

    if not amount.current.value.isdigit():
        amount.current.error_text = 'Este valor deve ser númerico'
        page.update()
        return

    amount.current.error_text = ''

    result = sorteio(
        k=int(amount.current.value),
        filename=Path(filename.current.value),
    )

    # greetings.current.controls.append(
    #     ft.Text(
    #         f'Sorteados em: {result}!',
    #     ),
    # )
    dlg = ft.AlertDialog(
        # modal=True,
        title=ft.Text('Sorteados:'),
        content=ft.Text(f'{result}'),
        on_dismiss=lambda _: logging.debug('dlg dismissed.'),
    )
    filename.current.value = ''
    amount.current.value = ''
    page.update()
    page.open(dlg)
    filename.current.focus()


def main_flet(page: ft.Page) -> None:
    """GUI para sorteio."""
    page.title = TITLE
    page.window_center = True
    page.window.width = 400
    page.window.height = 250
    page.window.min_width = 400
    page.window.min_height = 250
    page.add(
        ft.TextField(
            ref=filename,
            label='Arquivo Excel',
            autofocus=True,
        ),
        ft.TextField(ref=amount, label='Quantidade'),
        ft.ElevatedButton('Sortear', on_click=btn_click),
        ft.Column(ref=greetings),
    )


layout = [
    [
        sg.Text('Arquivo excel:'),
        sg.Input(key='filename'),
        sg.FileBrowse(file_types=(('Excel files', '*.xls*'),)),
    ],
    [sg.Text('Quantidade:'), sg.Input(key='quantia')],
    [sg.Exit(), sg.Button('Sortear')],
]
window = sg.Window('Sorteio XLSX', layout)


def main():
    """GUI para sorteio."""
    while 1:
        event, values = window.read()
        logging.debug(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Sortear':
            try:
                result = (
                    sorteio(
                        k=int(values['quantia']),
                        filename=Path(values['filename']),
                    ),
                )
                sg.popup_notify(result)
                logging.debug(result)
            except (FileNotFoundError, OSError, ValueError) as err:
                sg.popup_error(err)
    window.close()


if __name__ == '__main__':
    # main()
    ft.app(main_flet)
