import flet as ft
from flet import *

list_my_songs = ft.ListView(
        expand=1, 
        spacing=15, 
        padding=20, 
        auto_scroll=True,
)

#Estilo de tabla
table_info = DataTable( 
        heading_row_color='black',
        horizontal_lines=ft.border.BorderSide(1, "white"),
        column_spacing=50,
)
