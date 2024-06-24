"""Main module."""
# -*- coding: utf-8 -*-
# from incolume.py.sorteio_xlsx.sorteio import sorteio
from __future__ import annotations

import PySimpleGUI as sg


import flet as ft
from pathlib import Path

import datetime as dt
import random

import pandas as pd
import pytz
from typing import Final


TZ: Final = pytz.timezone('America/Sao_Paulo')
filename = ft.Ref[ft.TextField]()
amount = ft.Ref[ft.TextField]()
greetings = ft.Ref[ft.Column]()


# TODO @britodfbr: Fazer funcionar com importação de módulo.  # noqa: TD003 FIX002 E501
def sorteio(k: int = 1, filename: Path | None = None) -> Path:
    """Lotery by xlsx file."""
    filename = filename or Path(__file__).parent / 'empregados.xlsx'
    ext = {'.xlsx': pd.read_excel}
    timestamp = f'{(ts:=dt.datetime.now(tz=TZ)):-%Y-%m-%d-%H-%M-%S}'
    fout: Path = filename.with_name(
        f'{filename.stem}{timestamp}.xlsx',
    )
    df0 = ext.get(filename.suffix)(filename)

    items = list(df0.index)
    k = min(k, len(items))
    result = random.sample(items, k=k)

    df0.loc[result].to_excel(fout)
    return fout


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

    greetings.current.controls.append(
        ft.Text(
            f'Sorteados em: {result}!',
        ),
    )
    filename.current.value = ''
    amount.current.value = ''
    page.update()
    filename.current.focus()


def main_flet(page: ft.Page) -> None:
    """GUI para sorteio."""
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
        print(event, values)
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
                print(result)
            except (FileNotFoundError, OSError, ValueError) as err:
                sg.popup_error(err)
    window.close()


if __name__ == '__main__':
    main()
