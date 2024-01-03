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
user_name_log=ft.Text(
    font_family="SpaceMono",
    width=600,  
    height=50,
    size=20,
    weight='w900',
    text_align='left',
    color='white',
    bgcolor={
        #ft.MaterialState.DEFAULT:ft.colors.BLACK,
        ft.MaterialState.DEFAULT:ft.colors.BLACK,   
        ft.MaterialState.HOVERED:"#080808",     
    },
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