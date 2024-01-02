import re
from components import button_style as buttons
from components import txtFields_style as Ctxt

@staticmethod
def validTxt(page,user,password):
    
    if(user=='' and password==''):
        Ctxt.name_txtField.error_text = 'Ingrese usuario'
        Ctxt.pass_txtField.error_text = "ingrese contrasena"
        page.update()
    elif(user==''):
        Ctxt.name_txtField.error_text = 'Ingrese usuario'
        page.update()
    elif(password==''):
        Ctxt.pass_txtField.error_text = "ingrese contrasena"
        page.update()
    else:
        Ctxt.name_txtField.error_text = None
        Ctxt.pass_txtField.error_text = None
        page.update()

# Método para manejar el evento de hacer clic en "Sí" para salir
@staticmethod
def yes_click(e,page):
    page.window_destroy()

# Método para manejar el evento de hacer clic en "No" para seguir
@staticmethod
def no_click(e,page):
    buttons.confirm_dialog.open = False
    page.update()

# Método para manejar eventos de la ventana (cierre)
@staticmethod
def window_event(e,page):
    if e.data == "close":
        page.dialog = buttons.confirm_dialog
        buttons.confirm_dialog.open = True
        page.update()

# Método para manejar el evento de hacer clic en "iniciar sesion"
@staticmethod
def btn_startSession_click(e, page):
    user=Ctxt.name_txtField.value
    password=Ctxt.pass_txtField.value
    validTxt(page,user,password)
    #consulta BD


@staticmethod
def btn_registerPage_click(e, page):
    page.go('/register')

@staticmethod
def btn_registerAPI_click(e, page):
    page.go('/register')
    #Logica de spotify API

# Método para asignar eventos a elementos UI
def events(page):
    page.on_window_event = lambda e: window_event(e,page)
    buttons.btn_confirm.on_click = lambda e: yes_click(e,page)
    buttons.btn_deny.on_click = lambda e: no_click(e,page)
    buttons.btn_startSession.on_click = lambda e: btn_startSession_click(e,page)
    buttons.btn_register_i.on_click = lambda e: btn_registerPage_click(e,page)
    buttons.btn_register.on_click = lambda e: btn_registerAPI_click(e,page)
    #add btn for API

    #arbitrario noroeste salto de piedra