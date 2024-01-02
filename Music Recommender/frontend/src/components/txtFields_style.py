import flet as ft
from flet import *

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


#Estilo de los campos de entrada
reg_name_txtField =TextField(
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
reg_pass_txtField =TextField(
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