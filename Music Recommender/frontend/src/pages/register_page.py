import flet as ft
from components import button_style
from components import txtFields_style
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
                        Divider(height=140, color="transparent"),
                        Text(
                            "Registra tu cuenta con Spotify",
                            width=500,
                            size=20,
                            weight='w900',
                            text_align='center',
                        ),
                        Divider(height=15, color="transparent"),
                        Text(
                            "Ingresa tus datos",
                            width=500,
                            weight='w900',
                            text_align='center',
                            size=15,
                        ),
                        Divider(height=10, color="transparent"),
                        Container(
                            txtFields_style.reg_name_txtField,
                            padding=padding.only(left=75,right=40),
                        ),
                        Container(
                            txtFields_style.reg_pass_txtField,
                            padding=padding.only(left=75,right=40),
                        ),
                        Divider(height=5, color="transparent"),
                        Container(
                            button_style.btn_register,
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
