import re
import sys
import os
import flet as ft
current_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(parent_directory)

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

def validTxt(page,user,password):
    
    if(user=='' and password==''):
        Ctxt.name_txtField.error_text = 'Ingrese usuario'
        Ctxt.pass_txtField.error_text = "ingrese contrasena"
        page.update()
    elif(user=='' and password !=''):
        Ctxt.name_txtField.error_text = 'Ingrese usuario'
        Ctxt.pass_txtField.error_text = None
        page.update()
    elif(password=='' and user !=''):
        Ctxt.pass_txtField.error_text = "ingrese contrasena"
        Ctxt.pass_txtField.error_text = None
        page.update()
    else:
        Ctxt.name_txtField.error_text = None
        Ctxt.pass_txtField.error_text = None
        page.update()

def btn_startSession_click(e, page):
    user=Ctxt.name_txtField.value
    password=Ctxt.pass_txtField.value
    validTxt(page,user,password)
    #consulta BD
    page.go('/playlist')

def btn_registerPage_click(e, page):
    page.go('/register')

def log(e,page):
    page.login(provider)
    def on_login(e):
        if e.error:
            raise Exception(e.error)
        else:
            Listas.list_my_songs.clean()
            user='Tus 10 artistas mas escuchados '+page.auth.user.id 
            Ctxt.user_name_log.value=user
            artistas = AuthRequest.search_artist_most_played(page.auth.token.token_type,page.auth.token.access_token)
            for artista in artistas:
                Listas.list_my_songs.controls.append(ft.Text(artista,size=35,font_family="SpaceMono"))
            page.update()
    page.on_login = on_login
    page.go('/playlist')
    page.update()

def gen_recom(e,page):
    page.update()

# Método para asignar eventos a elementos UI
def events(page):
    buttons.btn_startSession.on_click = lambda e: btn_startSession_click(e,page)
    buttons.btn_register_i.on_click = lambda e: btn_registerPage_click(e,page)
    buttons.btn_register.on_click = lambda e: log(e,page)
    buttons.btn_gen_recom.on_click = lambda e: gen_recom(e,page)