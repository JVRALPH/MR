# Este script es el punto de entrada principal de la aplicación. Configura la página, las rutas y las vistas, así como los eventos asociados para la navegación y la interacción con la interfaz de usuario.

# Importaciones necesarias
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

# Definición de la función principal
def main(page: Page):
    # Configuración de fuentes y tema de la página
    page.fonts = {
        "Raleway" : "fonts/Raleway-Regular.ttf",
        "SpaceMono" : "fonts/SpaceMono-Bold.ttf"
    }
    page.theme = Theme(font_family="Raleway")

    # Función para cambiar la ruta
    def route_change(route):
        page.views.clear()# Limpia las vistas actuales
        page.views.append(# Añade la vista correspondiente según la ruta
            View(
                route='/',
                padding=0,
                scroll='ADAPTIVE',
                controls=[
                    index_page.form_body,# Vista para la página principal (index_page)]
                ]
            )
        )
        # Añade la vista para la página de lista de reproducción (playlist_page)
        if page.route == '/playlist':
            if EventMan.user_is_authenticated():
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
            else:
                page.go("/")
        # Actualiza la página con las nuevas vistas
        page.update()

    # Función para volver a la vista anterior
    def view_pop(view): 
        page.views.pop() # Elimina la última vista
        top_view = page.views[-1] # Navega de regreso a la vista superior
        page.go(top_view.route) # Asigna las funciones de cambio de ruta y navegación a eventos específicos de la página
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route) # Navega a la ruta actual
    Psett.page_settings(page)
    EventMan.events(page) # Asignación de eventos a elementos de la interfaz de usuario

# Inicia la aplicación Flet
ft.app(target=main,assets_dir='assets',view=WEB_BROWSER,port=8550)
