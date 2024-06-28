"""Flet interface module."""
# ruff: noqa: ERA001 T201

from __future__ import annotations
import logging
import flet as ft
from pathlib import Path
from incolume.py.sorteio_xlsx.sorteio import sorteio
from incolume.py.sorteio_xlsx import TITLE

filename = ft.Ref[ft.TextField]()
amount = ft.Ref[ft.TextField]()
greetings = ft.Ref[ft.Column]()
filepicker = ft.FilePicker()


def picker_file(e: ft.ControlEvent) -> None:
    """Get filename."""
    if not e.files:
        return
    filename.current.value = e.files[0].path
    e.page.update()


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


def interface_gui(page: ft.Page) -> None:
    """GUI para sorteio."""
    page.title = TITLE
    page.window_center = True
    page.window.width = 600
    page.window.height = 250
    page.window.min_width = 600
    page.window.min_height = 250

    pick_files_dialog = ft.FilePicker(
        on_result=picker_file,
    )

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.ResponsiveRow(
            alignment=ft.alignment.center,
            controls=[
                ft.Column(
                    col=9,
                    controls=[
                        ft.TextField(
                            ref=filename,
                            label='Arquivo Excel',
                            autofocus=True,
                        ),
                    ],
                ),
                ft.Column(
                    col=3,
                    controls=[
                        ft.ElevatedButton(
                            'Arquivos',
                            icon=ft.icons.UPLOAD_FILE,
                            on_click=lambda _: pick_files_dialog.pick_files(
                                allow_multiple=False,
                                file_type=ft.FilePickerFileType.CUSTOM,
                                allowed_extensions=['xlsx', 'xls', 'odt'],
                            ),
                        ),
                    ],
                ),
            ],
        ),
        ft.ResponsiveRow(
            col=12,
            controls=[
                ft.TextField(ref=amount, label='Quantidade'),
            ],
        ),
        ft.ElevatedButton('Sortear', on_click=btn_click),
        ft.Column(ref=greetings),
    )
