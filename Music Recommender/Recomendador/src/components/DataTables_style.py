# Clase que define varios componentes de interfaz de usuario 
# utilizando la librería 'flet'

# Importación de librerías necesarias
import flet as ft
from flet import *

# Definición de componentes de interfaz de usuario

# Avatar del usuario
user_image = CircleAvatar(
        radius=150
)

# Columna para mostrar las canciones del usuario
Col_song1 = Column(
        scroll=ft.ScrollMode.ALWAYS,
)

# Otra columna para mostrar las recomendaciones de canciones
Col_song2 = Column(
        scroll=ft.ScrollMode.ALWAYS,
)

# Lista para mostrar la información del usuario
list_user_info = ft.ListView(
        auto_scroll=False,
        expand=1,
        spacing=10,
        padding=20,
)

# ListTile para mostrar las canciones del usuario
list_my_songs = ft.ListTile(
        expand=1,
)

# Lista para mostrar las recomendaciones
list_recom = ft.ListView(
        expand=1,
        spacing=15,
        padding=20,
)

# Estilo de tabla para mostrar información detallada
table_info = DataTable(
        heading_row_color='black',
        horizontal_lines=ft.border.BorderSide(1, "white"),
        column_spacing=50,
)
