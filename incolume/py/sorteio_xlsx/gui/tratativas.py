"""Tatativa."""

import flet as ft


def tratativa3(page: ft.Page) -> None:
    """Tratativa."""
    filename = ft.Ref[ft.TextField]()
    amount = ft.Ref[ft.TextField]()

    def picker_file(e: ft.ControlEvent):
        """Get filename."""
        if not e.files:
            return
        filename.current.value = e.files[0].path

        e.page.update()

    pick_files_dialog = ft.FilePicker(
        on_result=picker_file,
    )

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.TextField(
                    ref=filename,
                    label='Nome do Arquivo',
                    hint_text='Arquivo excel .. ',
                ),
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
        ft.Row(controls=[ft.TextField(ref=amount, label='quantidade')]),
    )


def tratativa2(page: ft.Page) -> None:
    """Tratativa."""
    filename = ft.Ref[ft.TextField]()
    amount = ft.Ref[ft.TextField]()

    def picker_file(e: ft.FilePickerResultEvent):
        """Get filename."""
        if not e.files:
            return
        filename.current.value = e.files[0].path

        page.update()

    pick_files_dialog = ft.FilePicker(
        on_result=picker_file,
    )

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.TextField(
                    ref=filename,
                    label='Nome do Arquivo',
                    hint_text='Arquivo excel .. ',
                ),
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
        ft.Row(controls=[ft.TextField(ref=amount, label='quantidade')]),
    )


def tratativa1(page: ft.Page) -> None:
    """Tratativa."""
    filename = ft.Ref[ft.TextField]()
    amount = ft.Ref[ft.TextField]()

    def picker_file(e: ft.FilePickerResultEvent):
        """Get filename."""
        filename.current.value = e.files[0].path
        page.update()

    pick_files_dialog = ft.FilePicker(
        on_result=picker_file,
    )

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.TextField(
                    ref=filename,
                    label='Nome do Arquivo',
                    hint_text='Arquivo excel .. ',
                ),
                ft.ElevatedButton(
                    'Arquivos',
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=False,
                    ),
                ),
            ],
        ),
        ft.Row(controls=[ft.TextField(ref=amount, label='quantidade')]),
    )


def tratativa0(page: ft.Page) -> None:
    """Tratativa."""
    filename = ft.Ref[ft.TextField]()
    amount = ft.Ref[ft.TextField]()
    pick_files_dialog = ft.FilePicker(
        on_result=lambda e: print(e.files[0].path),
    )

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.TextField(
                    ref=filename,
                    label='Nome do Arquivo',
                    hint_text='Arquivo excel .. ',
                ),
                ft.ElevatedButton(
                    'Pick files',
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=False,
                    ),
                ),
            ],
        ),
    )


def main(page: ft.Page) -> None:
    """Exemplo oficial."""

    def pick_files_result(e: ft.FilePickerResultEvent) -> None:
        """Function."""
        selected_files.value = (
            ', '.join(map(lambda f: f.name, e.files))
            if e.files
            else 'Cancelled!'
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    'Pick files',
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True,
                    ),
                ),
                selected_files,
            ],
        ),
    )
