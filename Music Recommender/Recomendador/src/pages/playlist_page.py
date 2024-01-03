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
            Row([
                Container(
                    content=Card(
                        width=600,
                        height=600,
                        elevation=20,
                        content=Container(
                            Column([
                                Ctext.user_name_log,
                                Listas.list_my_songs,
                            ],
                            alignment=ft.alignment.top_center),
                            padding=padding.only(left=50,top=15),
                        ),
                    ),
                ),
                ft.VerticalDivider(color="transparent"),
                Container(
                    #offset=transform.Offset(0,0),
                    #animate_offset=animation.Animation(900),
                    content=Card(
                        width=600,
                        height=600,
                        elevation=20,
                        content=Container(
                            Column([
                                btns.btn_gen_recom,
                            ],
                            alignment=ft.alignment.top_center),
                            padding=padding.only(left=150,top=15),
                        ),
                    )
                ),
            ]),
        ]),
    ]),
    padding=80,
    width=1920,
    height=1080,
    gradient=RadialGradient(
        center=Alignment(0,-1.25),
        radius=1.4,
        colors=["#42445f","#393b52","#33354a","#2f3143","#292b3c","#222331","#1a1a25","#1a1b26","#21222f","#1d1e2a"],
        ),
    
)