import flet as ft
from flet import *

user_image=CircleAvatar(
        radius=150
)

Col_song1 = Column(    
        scroll=ft.ScrollMode.ALWAYS,
)
Col_song2 = Column(
        scroll=ft.ScrollMode.ALWAYS,
)

list_user_info = ft.ListView(
        auto_scroll=False,
        expand=1, 
        spacing=10, 
        padding=20, 
)

list_my_songs = ft.ListTile(
        expand=1, 
)

list_recom = ft.ListView(
        expand=1, 
        spacing=15, 
        padding=20, 
)
#Estilo de tabla
table_info = DataTable( 
        heading_row_color='black',
        horizontal_lines=ft.border.BorderSide(1, "white"),
        column_spacing=50,
)
