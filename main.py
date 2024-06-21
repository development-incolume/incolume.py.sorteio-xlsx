"""Main module."""

import flet as ft
from pathlib import Path
from incolume.py.sorteio_xlsx.sorteio import sorteio

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

    greetings.current.controls.append(
        ft.Text(
            f'Sorteados em: {result}!',
        ),
    )
    filename.current.value = ''
    amount.current.value = ''
    page.update()
    filename.current.focus()


def main(page: ft.Page) -> None:
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


if __name__ == '__main__':
    ft.app(main)
