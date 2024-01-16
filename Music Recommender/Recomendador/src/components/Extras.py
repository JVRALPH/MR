# Clase que define varios componentes de interfaz de usuario 
# utilizando la librería 'flet'

# Importación de librerías necesarias
import flet as ft
from services import EventMan as event
# Definición de componentes de interfaz de usuario

rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        extended=False,
        min_width=100,
        min_extended_width=500,
        group_alignment=-1,
        destinations=[
                ft.NavigationRailDestination(
                        icon=ft.icons.HOME, 
                        selected_icon=ft.icons.HOME_FILLED, 
                        label="Inicio"
                ),
                ft.NavigationRailDestination(
                        icon=ft.icons.FAVORITE_BORDER, 
                        selected_icon=ft.icons.FAVORITE, 
                        label="Favoritos"
                ),
                ft.NavigationRailDestination(
                        icon_content=ft.Icon(ft.icons.LOGOUT_OUTLINED),
                        selected_icon_content=ft.Icon(ft.icons.LOGOUT_SHARP),
                        label="Salir"
                )
        ],
        bgcolor="transparent",
)


save_fav = ft.Chip(
        label=ft.Text("Save to favorites"),
        leading=ft.Icon(ft.icons.FAVORITE_BORDER_OUTLINED),
        bgcolor=ft.colors.TRANSPARENT,
        disabled_color=ft.colors.TRANSPARENT,
        autofocus=True,
)