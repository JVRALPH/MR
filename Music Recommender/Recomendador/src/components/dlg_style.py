import flet as ft
from flet import *

dlg = ft.AlertDialog(
    title=ft.Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
)