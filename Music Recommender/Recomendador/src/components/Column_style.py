# Clase que define varios componentes de interfaz de usuario 
# utilizando la librería 'flet'

# Importación de librerías necesarias
import flet as ft
from flet import *

# Definición de componentes de interfaz de usuario

# Columna para mostrar las canciones del usuario
Col_song1 = Column(
        scroll=ft.ScrollMode.ALWAYS,
)

# Otra columna para mostrar las recomendaciones de canciones
Col_song2 = Column(
        scroll=ft.ScrollMode.ALWAYS,
)
