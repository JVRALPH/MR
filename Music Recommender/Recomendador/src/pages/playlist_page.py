import flet as ft
import sys,os

current_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(parent_directory)

from services import AuthRequest
from components import txtFields_style as Ctext
from components import button_style as btns
from components import DataTables_style as Listas
from flet import *
from math import pi

#Estilo page principal
form_songs = Container(
    #Ctext.user_name_log,
    Stack([
        Column([
            ft.Text("MUSIC RECORD",text_align="center",font_family="SpaceMono",size=20),
            Row([
                ft.Stack(
                    [
                        Listas.user_image,
                        ft.Container(
                            content=ft.CircleAvatar(bgcolor=ft.colors.GREEN, radius=8),
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
                    Listas.list_user_info,
                    alignment=ft.alignment.top_center,
                    ),
                ),
            ]),
            Divider(color="transparent"),
            Row([
                btns.btn_get_songs,
                VerticalDivider(color="transparent"),
                btns.btn_gen_recom,
            ]),
            Divider(color="transparent"),
            Row([
                ft.Text("Canciones mas escuchadas",width=600,size=20,font_family="SpaceMono"),
                VerticalDivider(color="transparent"),
                ft.Text("Canciones recomendadas",width=600,size=20,font_family="SpaceMono"),
            ]),
            Divider(color="transparent"),
            Row([
                Card(
                    width=600,
                    height=600,
                    elevation=20,
                    content=Container(
                        Listas.Col_song1,
                        alignment=ft.alignment.top_center
                    ),
                ),
                VerticalDivider(color="transparent"),
                Card(
                    width=600,
                    height=600,
                    elevation=20,
                    content=Container(
                        Listas.Col_song2,
                        alignment=ft.alignment.top_center,
                    ),
                ),
            ]),
            Divider(visible=False,height=15)
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