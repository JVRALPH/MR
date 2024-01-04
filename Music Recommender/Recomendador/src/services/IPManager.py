import re
import sys
import os
import flet as ft
current_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(parent_directory)

from components import dlg_style as dlgs
from components import DataTables_style as Listas
from components import button_style as buttons
from components import txtFields_style as Ctxt
from services import AuthRequest
from flet.auth import OAuthProvider
from dotenv import load_dotenv


load_dotenv()
provider = OAuthProvider(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    authorization_endpoint="https://accounts.spotify.com/authorize?",
    token_endpoint="https://accounts.spotify.com/api/token",
    user_scopes=["user-read-private user-read-email user-top-read user-library-read"],
    redirect_url="http://localhost:8550/api/oauth/redirect",
    user_endpoint="https://api.spotify.com/v1/me",
    user_id_fn=lambda u: u["id"],
)
class TokenManager:
    def __init__(self):
        self.access_token = None

    def set_token(self, access_token):
        self.access_token = access_token

    def get_token(self):
        return self.access_token
    
token_manager = TokenManager()

def validTxt(page,user,password):
    Ctxt.name_txtField.error_text = 'Ingrese usuario' if user == '' else None
    Ctxt.pass_txtField.error_text = 'Ingrese contraseña' if password == '' else None
    page.update()

def btn_startSession_click(e, page):
    user=Ctxt.name_txtField.value
    password=Ctxt.pass_txtField.value
    validTxt(page,user,password)

    #consulta BD
    if(user!='' and password!=''):
        page.go('/playlist')

def btn_registerPage_click(e, page):
    page.go('/register')

def log(e, page):
    def on_login(e):
        if e.error:
            page.go('/')
            alert_title = ft.Text("Error de inicio de sesión")
            alert_content = ft.Text("No se pudo registrar usuario. Inténtalo de nuevo más tarde.")
            error_dialog = ft.AlertDialog(title=alert_title, content=alert_content)
            page.dialog = error_dialog
            error_dialog.open = True  # Abrir la alerta de diálogo
            page.update()
        else:
            Listas.list_my_songs.clean()
            user = ['Tus 10 canciones mas escuchados ' + page.auth.user.id]
            Ctxt.user_name_log.value = user[0]
            token_manager.set_token(page.auth.token.access_token)
            artistas = AuthRequest.search_tracks_most_played(page.auth.token.token_type, token_manager.get_token())
            for artista in artistas:
                Listas.list_my_songs.controls.append(ft.Text(artista, size=20, font_family="Raleway"))
            page.update()
    page.login(provider)
    page.on_login = on_login
    page.go('/playlist')
    page.update()
    

def gen_recom(e, page):
    access_token = token_manager.get_token()
    if access_token:
        Listas.list_recom.clean()
        recomendaciones = AuthRequest.gen_recom_tracks(page.auth.token.token_type, token_manager.get_token())
        for canciones in recomendaciones:
                Listas.list_recom.controls.append (ft.Text(canciones, size=20, font_family="Raleway"))
        page.update()
    else:
        print("No se ha obtenido el access_token aún.")

# Método para asignar eventos a elementos UI
def events(page):
    buttons.btn_startSession.on_click = lambda e: btn_startSession_click(e,page)
    buttons.btn_register_i.on_click = lambda e: btn_registerPage_click(e,page)
    buttons.btn_register.on_click = lambda e: log(e,page)
    buttons.btn_gen_recom.on_click = lambda e: gen_recom(e,page)