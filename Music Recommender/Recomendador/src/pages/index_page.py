import flet as ft
import sys,os
current_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(parent_directory)

from components import button_style as Cbtn
from components import txtFields_style as Ctext
from flet import *
from math import pi

#Estilo page principal
form_body = Container(
    Container(
        Stack([
            Container(
                border_radius=11,
                rotate=Rotate(0.98*pi), #degree
                width=500,
                height=620,
                bgcolor="#11ffffff",
            ),
            Container(
                Container(
                    Column([
                        Container(
                            Icon(
                                ft.icons.LIBRARY_MUSIC_OUTLINED,
                                size=100,
                            ),padding=padding.only(left=180,top=30),
                        ),
                        Text(
                            "Recomendador de musica",
                            width=500,
                            size=20,
                            weight='w900',
                            text_align='center',
                        ),
                        Divider(height=15, color="transparent"),
                        Text(
                            "Porfavor ingresa tu cuenta y contrasena",
                            width=500,
                            weight='w600',
                            text_align='center',
                            size=10,
                        ),
                        Divider(height=10, color="transparent"),
                        Container(
                            Ctext.name_txtField,
                            padding=padding.only(left=75,right=40),
                        ),
                        Container(
                            Ctext.pass_txtField,
                            padding=padding.only(left=75,right=40),
                        ),
                        Divider(height=5, color="transparent"),
                        Container(
                            Cbtn.btn_startSession,
                            padding=padding.only(left=75,right=40,bottom=0),   
                        ),
                        Container(
                            Cbtn.btn_register_i,
                            padding=padding.only(left=75,right=40,bottom=0),   
                        ),
                    ])
                ),
                #First straight box
                width=500,
                height=620,
                bgcolor="#11ffffff",
                border_radius=11,
                
            ),
            
        ]),
        
        #Where every elements start
        padding=80,
        alignment=ft.alignment.top_center,
        width=500,
        height=900,
    ),
    width=1920,
    height=1080,
    gradient=LinearGradient(
        colors=["#4d194d","#3e1f47","#312244","#272640","#212f45","#1b3a4b","#144552","#0b525b","#065a60","#006466"],
        #rotation=(pi*1.5),
        rotation=(pi*0.5),
    ),
)
