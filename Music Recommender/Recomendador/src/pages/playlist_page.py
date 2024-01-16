
# En esta sección se configura la página principal de la aplicación con diferentes estilos y elementos visuales.

# Importaciones necesarias
import flet as ft
import sys,os

current_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(parent_directory)

from services import AuthRequest # Importa los servicios de autenticación
from components import txtFields_style as Ctext # Importa estilos para campos de texto
from components import button_style as btns # Importa estilos para botones
from components import DataTables_style as Listas  # Importa estilos para tablas
from components import Column_style as columna
from components import Avatar_style as avatar
from components import Extras as ext

from flet import *
from math import pi

#Estilo page principal
form_songs = Container(
    Stack([
        Row([
            ext.rail,
            ft.VerticalDivider(width=1,color="transparent"),
            Column([
                ft.Text("MUSIC RECORD",text_align="center",font_family="SpaceMono",size=20),  # Título de la aplicación
                Row([
                    ft.Stack(
                        [
                            avatar.user_image, # Imagen de usuario
                            ft.Container(
                                content=avatar.user_state,# Estado del usuario (círculo verde)
                                alignment=ft.alignment.bottom_left,
                            ),
                        ],
                        width=100,
                        height=100,
                    ),
                    Card(
                        width=1130,
                        height=200,
                        elevation=20,
                        content=Container(
                        Listas.list_user_info,# Lista de información del usuario
                        alignment=ft.alignment.top_center,
                        ),
                    ),
                ]),
                Divider(color="transparent"),
                # Botones para obtener canciones y generar recomendaciones
                Row([
                    btns.btn_get_songs,
                    VerticalDivider(color="transparent"),
                    btns.btn_gen_recom,
                ]),
                Divider(color="transparent"),
                # Títulos de secciones de canciones más escuchadas y recomendadas
                Row([
                    ft.Text("Canciones mas escuchadas",width=600,size=20,font_family="SpaceMono"),
                    VerticalDivider(color="transparent"),
                    ft.Text("Canciones recomendadas",width=600,size=20,font_family="SpaceMono"),
                ]),
                Divider(color="transparent"),
                # Visualización de canciones más escuchadas y recomendadas en tarjetas
                Row([
                    Card(
                        width=600,
                        height=600,
                        elevation=20,
                        content=Container(
                            columna.Col_song1,# Columna de canciones más escuchadas
                            alignment=ft.alignment.top_center
                        ),
                    ),
                    VerticalDivider(color="transparent"),
                    Card(
                        width=600,
                        height=600,
                        elevation=20,
                        content=Container(
                            columna.Col_song2,# Columna de canciones recomendadas
                            alignment=ft.alignment.top_center,
                        ),
                    ),
                ]),
                Divider(visible=False,height=15)
            ]),
        ]),
    ]),



    padding=padding.only(bottom=200,left=50,top=15),
    width=1920,
    height=1080,
    gradient=RadialGradient(
        center=Alignment(0,-1.25),
        radius=1.4,
        colors=["#42445f","#393b52","#33354a","#2f3143","#292b3c","#222331","#1a1a25","#1a1b26","#21222f","#1d1e2a"],
        ),
)