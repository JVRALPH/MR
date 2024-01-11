# Clase que define varios componentes de interfaz de usuario 
# utilizando la librería 'flet'

# Importación de librerías necesarias
import flet as ft
from flet import *

# Definición de componentes de interfaz de usuario
# Lista para mostrar la información del usuario
list_user_info = ft.ListView(
        auto_scroll=False,
        expand=1,
        spacing=10,
        padding=20,
)

# Estilo de tabla para mostrar información detallada
table_info = DataTable(
        heading_row_color='black',
        horizontal_lines=ft.border.BorderSide(1, "white"),
        column_spacing=50,
)
