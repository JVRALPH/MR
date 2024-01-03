import flet as ft
from flet import *
from math import pi

    #Estilos de botones

btn_gen_recom=ElevatedButton(
    content=Text(
        "Generar recomendaciones",
        color='white',
    ),
    style=ButtonStyle(
        shape=RoundedRectangleBorder(radius=10),
    ),
    bgcolor={
        #ft.MaterialState.DEFAULT:ft.colors.BLACK,
        ft.MaterialState.DEFAULT:ft.colors.BLACK,   
        ft.MaterialState.HOVERED:"#080808",     
    },
    width=300,
    height=50,
)

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

btn_register_i=ElevatedButton(
    tooltip="Aun no tienes cuenta?, Ingresa con Spotify",
    content=Text(
        "Registrar",
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
