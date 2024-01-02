import flet as ft
from components import pagesettings_style as Psett
from pages import index_page
from pages import playlist_page
from pages import register_page
from services import IPManager
from flet import *

# Función principal que maneja la aplicación
def main(page: Page):

    # Función para cambiar de ruta
    def route_change(route):
        # Borra las vistas actuales
        page.views.clear()
        # Añade la vista principal del formulario
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
        if page.route == '/register':
            page.views.append(
                View(
                route='/',
                padding=0,
                scroll='ADAPTIVE',
                controls=[
                    #AppBar(title=Text('Regresar'), bgcolor='black', toolbar_height=40),
                    register_page.form_body,
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
                        playlist_page.form_body,
                    ]
                )
            )
        # Actualiza la página con las nuevas vistas
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

    # Configuración adicional de la página a través de la clase UIElements
    Psett.page_settings(page)

    # Asigna eventos a la clase IPManager
    IPManager.events(page)

# Inicia la aplicación con la función principal
ft.app(target=main,view=WEB_BROWSER,port=8550)
