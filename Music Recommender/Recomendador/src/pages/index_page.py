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
                width=800,
                height=800,
                bgcolor="#11ffffff",
            ),
            Container(
                Container(
                    Column([
                        Container(
                            Icon(
                                ft.icons.LIBRARY_MUSIC_OUTLINED,
                                size=100,
                            ),padding=padding.only(left=200,top=30),
                        ),
                        Text(
                            "MUSIC RECORD",
                            width=500,
                            size=20,
                            weight='w900',
                            text_align='center',
                        ),
                        Divider(height=15, color="transparent"),
                        Text(
                            "Bienvenido a nuestra aplicación MusicRecord es una plataforma diseñada para ofrecer a los usuarios una experiencia personalizada y atractiva al descubrir nueva música y gestionar sus listas de reproducción. Con una integración directa con la plataforma Spotify, permite a los usuarios acceder y explorar una amplia gama de pistas musicales. Nuestro objetivo es ofrecer una experiencia musical personalizada y agradable, permitiendo a los usuarios descubrir nuevas canciones, gestionar sus gustos musicales y disfrutar de una amplia variedad de música de manera intuitiva y fácil.",
                            width=500,
                            weight='w600',
                            text_align='JUSTIFY',
                            size=20,
                            font_family="Raleway"
                        ),
                        Container(
                            Cbtn.btn_register,
                            padding=padding.only(left=50,right=40,bottom=0),   
                        ),
                        
                    ]),
                    padding=padding.only(left=150),
                    alignment=ft.alignment.top_center,
                ),
                width=800,
                height=800,
                bgcolor="#11ffffff",
                border_radius=11,
                
            ),
            
        ]),
        padding=80,
        alignment=ft.alignment.top_center,
        width=500,
        height=900,
    ),
    width=1920,
    height=1080,
    gradient=RadialGradient(
        center=Alignment(0,-1.25),
        radius=1.4,
        colors=["#0d1321","#1d2d44","#2E455D","#3e5c76","#597491","#748cab","#B2BCC2","#f0ebd8"],
    ),
)
