import flet as ft
import sys,os
current_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(parent_directory)

from components import pagesettings_style as Psett
from pages import index_page
from pages import playlist_page
from services import EventMan
from flet import *

def main(page: Page):
    page.fonts = {
        "Raleway" : "fonts/Raleway-Regular.ttf",
        "SpaceMono" : "fonts/SpaceMono-Bold.ttf"
    }
    page.theme = Theme(font_family="Raleway")

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                route='/',
                padding=0,
                scroll='ADAPTIVE',
                controls=[
                    index_page.form_body,
                ]
            )
        )
        if page.route == '/playlist':
            page.views.append(
                View(
                    route='/',
                    padding=0,
                    scroll='ADAPTIVE',
                    controls=[
                        #AppBar(title=Text('Regresar'), bgcolor='black', toolbar_height=40),
                        playlist_page.form_songs,
                    ]
                )
            )
        page.update()

    # Función para volver a la vista anterior
    def view_pop(view):
        # Elimina la última vista
        page.views.pop()
        # Navega de regreso a la vista superior
        top_view = page.views[-1]
        page.go(top_view.route)
    # Asigna las funciones de cambio de ruta y navegación a eventos específicos de la página
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    # Navega a la ruta actual
    page.go(page.route)
    Psett.page_settings(page)
    EventMan.events(page)

ft.app(target=main,assets_dir='assets',view=WEB_BROWSER,port=8550)
