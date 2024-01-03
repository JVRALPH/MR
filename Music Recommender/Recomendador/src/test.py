import flet as ft

def main(page: ft.Page):
    def items(count):
        items = []
        for i in range(3):
            items.append(
            ft.Container(
                content=ft.Text(value=str(i)),
                alignment=ft.alignment.center
            )
        )
        return items

    def midcolumn_with_alignment(align: ft.MainAxisAlignment):
        return ft.Column(
            [
                
                ft.Container(
                    content=ft.Column(canvas, alignment=align),
                ),
            ]
        )
    def column_with_alignment(align: ft.MainAxisAlignment):
        return ft.Column(
        [
        
            ft.Container(
                content=ft.Column(items(3), alignment=align),
                height=400,
            ),
        ]
    )
    canvas = []
    canvas.append(
        ft.Container(
        content=ft.Text("Game field"),alignment=ft.alignment.center, width=500, height=500,bgcolor=ft.colors.TEAL
        )
    )

    page.add(
        ft.Row(
            [
                column_with_alignment(ft.MainAxisAlignment.START),
                midcolumn_with_alignment(ft.MainAxisAlignment.CENTER),
                column_with_alignment(ft.MainAxisAlignment.END),
                
            ],
            spacing=30,
            alignment=ft.MainAxisAlignment.START,
        )
    )

ft.app(target=main)