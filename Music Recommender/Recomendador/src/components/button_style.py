import flet as ft
from flet import *
from math import pi

    #Estilos de botones
btn_logout=IconButton(
    icon=ft.icons.LOGOUT_OUTLINED,
    icon_color="blue400",
    icon_size=20,
    tooltip="Cerrar Sesion",
)
btn_get_songs=ElevatedButton(
    content=Text(
        "Obtener canciones",
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
    width=600,
    height=50,
)

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
    width=600,
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
    tooltip="Click",
    content=Text(
        "INGRESAR CON SPOTIFY",
        color='white',
        size=15,
    ),
    width=400,
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
