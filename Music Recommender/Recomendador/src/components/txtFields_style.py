#Clase para configurar estilos de campos de entrada y elementos visuales utilizando la librería flet.

import flet as ft
from flet import *

# Estilos de campos de entrada y elementos visuales

# Estilo del campo de entrada para el nombre de usuario en el inicio de sesión
name_txtField = TextField(
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

# Texto para mostrar el nombre de usuario
user_name_log = ft.Text(
    font_family="SpaceMono",
    width=600,
    height=50,
    size=20,
    weight='w900',
    text_align='left',
    color='white',
    bgcolor={
        ft.MaterialState.DEFAULT: ft.colors.BLACK,
        ft.MaterialState.HOVERED: "#080808",
    },
)

# Configuración del campo de entrada para la contraseña en el inicio de sesión
pass_txtField = TextField(
    tooltip="Ingresa tu contraseña",
    password=True,
    can_reveal_password=True,
    width=300,
    height=70,
    hint_text='Contraseña: ',
    border_color=ft.colors.WHITE,
    border='underline',
    color='white',
    prefix_icon=icons.PASSWORD_OUTLINED,
    border_radius=11,
)

# Estilo del campo de entrada para el nombre de usuario en el registro
reg_name_txtField = TextField(
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

# Configuración del campo de entrada para la contraseña en el registro
reg_pass_txtField = TextField(
    tooltip="Ingresa tu contraseña",
    password=True,
    can_reveal_password=True,
    width=300,
    height=70,
    hint_text='Contraseña: ',
    border_color=ft.colors.WHITE,
    border='underline',
    color='white',
    prefix_icon=icons.PASSWORD_OUTLINED,
    border_radius=11,
)
