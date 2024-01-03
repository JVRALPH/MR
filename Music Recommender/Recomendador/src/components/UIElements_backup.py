import flet as ft
from flet import *
from math import pi
import IPManager as IPM

#Clase que maneja los elementos en las vistas
class UIElements:

    #Configuracion general de pagina
    def page_settings(page):
        page.window_prevent_close = True
        page.window_width=1920
        page.window_height=1080
        page.window_min_width=680
        page.window_min_height=800
        page.horizontal_alignment = 'center'
        page.vertical_alignment = 'center'
        page.padding=0
        page.window_resizable = True
        page.window_center()
        page.window_to_front()

    #Estilo de los campos de entrada
    name_txtField =TextField(
        tooltip="Ingresa tu usuario",
        width=300,
        height=70,
        hint_text='Usuario: ',
        border_color=ft.colors.WHITE,
        border='underline',
        color='white',
        prefix_icon=icons.ACCOUNT_CIRCLE_OUTLINED,
        border_radius=11,
    )

    #Configuracion de menu desplegable para el prefijo 
    pass_txtField =TextField(
        tooltip="Ingresa tu contrasena",
        password=True,
        can_reveal_password=True,
        width=300,
        height=70,
        hint_text='Contrasena: ',
        border_color=ft.colors.WHITE,
        border='underline',
        color='white',
        prefix_icon=icons.PASSWORD_OUTLINED,
        border_radius=11,
    )
    
    #Estilos de textos
    ip_text=Text(
        "Cuenta: ",
        width=800,
        size=20,
        weight='w900',
        text_align='center',
    )
    
    #Estilo de tabla
    table_info = DataTable( 
        heading_row_color='black',
        horizontal_lines=ft.border.BorderSide(1, "white"),
        column_spacing=50,
    )
    
    #Estilos de botones
    
    btn_startSession=ElevatedButton(
        
        content=Text(
            "Iniciar Sesion",
            color='white',
        ),
        width=300,
        height=50,
        style=ButtonStyle(
            shape=RoundedRectangleBorder(radius=10),
        ),
        bgcolor={
            
            #ft.MaterialState.DEFAULT:ft.colors.BLACK,
            ft.MaterialState.DEFAULT:ft.colors.BLACK,   
            ft.MaterialState.HOVERED:"#080808",     
        }
    )

    btn_register=ElevatedButton(
        tooltip="Aun no tienes cuenta?, Ingresa con Spotify",
        content=Text(
            "Registrar con spotify",
            color='white',
        ),
        width=300,
        height=50,
        style=ButtonStyle(
            shape=RoundedRectangleBorder(radius=10),
        ),
        bgcolor={
            ft.MaterialState.DEFAULT:"#199D47",   
            ft.MaterialState.HOVERED:"#189644",     
        }
    )

    btn_confirm=ElevatedButton(
        text="Si, quiero salir",
    )
    btn_deny=ElevatedButton(
        text="No",
    )

    #Estilo de dialogo de confirmacion para salir
    confirm_dialog = ft.AlertDialog(
        modal=False,
        title=ft.Text("Confirmacion"),
        content=ft.Text("¿Realmente quieres salir de esta aplicación?"),
        actions=[
            btn_confirm,
            btn_deny,
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

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
                                ),padding=padding.only(left=200,top=30),
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
                                name_txtField,
                                padding=padding.only(left=90,right=40),
                            ),
                            Container(
                                pass_txtField,
                                padding=padding.only(left=90,right=40),
                            ),
                            Divider(height=5, color="transparent"),
                            Container(
                                    btn_startSession,
                                    padding=padding.only(left=90,right=40,bottom=0),   
                            ),
                            Container(
                                    btn_register,
                                    padding=padding.only(left=90,right=40,bottom=0),   
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
    
    #Estilo de la pagina con tabla de informacion
    table_body = Container(
        Container(
            Stack([
                    Container(
                        Column([
                            Divider(height=25, color="transparent"),
                            table_info,
                        ])
                        ,padding=padding.only(0,20),
                    ),
            ]),
            padding=40,
            alignment=ft.alignment.top_center,
            width=1920,
            height=1080,
        ),
        width=1920,
        height=1080,
        gradient=LinearGradient(["#444444","#222222","#000000"]),
    )
