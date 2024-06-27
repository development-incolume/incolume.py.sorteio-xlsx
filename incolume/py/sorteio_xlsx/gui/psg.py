"""PySimpleGUI interface module."""

from __future__ import annotations
import logging
from pathlib import Path
from incolume.py.sorteio_xlsx.sorteio import sorteio
import PySimpleGUI as sg  # noqa: N813


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


def interface_gui():
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
