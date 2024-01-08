# Creación de un diálogo de alerta usando la librería 'flet'

# Importación de librerías necesarias
import flet as ft
from flet import *

# Creación de un diálogo de alerta
dlg = ft.AlertDialog(
    title=ft.Text("Hello, you!"),  # Título del diálogo
    on_dismiss=lambda e: print("Dialog dismissed!")  # Acción a realizar al cerrar el diálogo
)
