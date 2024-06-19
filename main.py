import flet as ft


def main(page: ft.Page):
    """GUI para sorteio"""
    filename = ft.Ref[ft.TextField]()
    amount = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    def btn_click(e):
        if not filename.current.value:
            filename.current.error_text = 'Please enter with Excel Filename'
            page.update()
            return

        filename.current.error_text = ''

        if not amount.current.value:
            amount.current.error_text = 'Please enter with amount'
            page.update()
            return

        amount.current.error_text = ''

        greetings.current.controls.append(
            ft.Text(
                f'Hello, {filename.current.value}' f' {amount.current.value}!',
            ),
        )
        filename.current.value = ''
        amount.current.value = ''
        page.update()
        filename.current.focus()

    page.add(
        ft.TextField(
            ref=filename,
            label='Excel Filename',
            autofocus=True,
        ),
        ft.TextField(ref=amount, label='Amount'),
        ft.ElevatedButton('Say hello!', on_click=btn_click),
        ft.Column(ref=greetings),
    )


if __name__ == '__main__':
    ft.app(main)
