# Configuración de la página usando la librería 'flet'

# Importación de librerías necesarias
import flet as ft
from flet import *

# Función para configurar la página
def page_settings(page):
    page.window_prevent_close = True  # Evitar el cierre de la ventana
    page.window_width = 1920  # Establecer el ancho de la ventana
    page.window_height = 1080  # Establecer la altura de la ventana
    page.horizontal_alignment = 'center'  # Alineación horizontal al centro
    page.vertical_alignment = 'center'  # Alineación vertical al centro
    page.padding = 10  # Establecer el relleno de la página
    page.title = "Music Record"  # Título de la página
