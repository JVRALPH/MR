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

def show_error_dialog(page):
    page.go('/')
    alert_title = ft.Text("Error de inicio de sesión")
    alert_content = ft.Text("No se pudo ingresar. Inténtalo de nuevo más tarde.")
    error_dialog = ft.AlertDialog(title=alert_title, content=alert_content)
    page.dialog = error_dialog
    error_dialog.open = True
    page.update()

def user_is_authenticated():
    access_token = token_manager.get_token()
    return access_token is not None

def get_user_info(page):
    token_manager.set_token(page.auth.token.access_token)
    user = page.auth.user.id
    user_info = AuthRequest.get_user_info(page.auth.token.token_type, token_manager.get_token(), user)
    
    if user_info:
        user_data = user_info[0]
        Listas.list_user_info.clean()
        images = user_data.get('images', [])
        if images and isinstance(images[0], str):
            Listas.user_image.foreground_image_url=images[0]
        fields = [
            ("Bienvenido Usuario: ", user_data.get('display_name', '')),
            ("ID del usuario: ", user_data.get('user_id', '')),
            ("Followers: ", str(user_data.get('followers', 0))),
        ]
        for field_name, field_value in fields:
            Listas.list_user_info.controls.append(ft.Text(value=f"{field_name}: {field_value}", size=25,font_family="Raleway"))
        
        page.update()
    else:
        show_error_dialog(page)

def logout_button_click(e,page):
    page.client_storage.remove(token_manager.get_token())
    page.logout()
    page.go('/')

def get_songs_user(e,page):
    access_token = token_manager.get_token()
    if access_token:
        Listas.Col_song1.clean()
        artistas = AuthRequest.search_tracks_most_played(page.auth.token.token_type, token_manager.get_token())
        num_can = 1
        for item in artistas:
            cancion_artista = item['cancion_artista']
            image_url = item['image_url'] 
            song_id = item['id']  # Obtener el ID de la canción
            
            cancion, artista = cancion_artista.split(" - ")  # Suponiendo que el formato sea "Cancion - Artista"            
            # Crea el ListTile con la imagen de la canción
            tile = ft.ListTile(
                leading=ft.Image(src=image_url, width=50, height=350),  # La imagen de la canción
                title=ft.Text(cancion, size=20, font_family="Raleway"),  # El título será el nombre de la canción
                subtitle=ft.Text(artista, size=15, font_family="Raleway"),  # El subtítulo será el nombre del artista
                trailing=ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(
                            text="Escuchar",
                            on_click=lambda _, song_id=song_id: open_spotify_link(song_id,page),
                        ),
                    ],
                ),
                tooltip = f"{num_can}° Cancion mas escuchada"
            )
            num_can += 1
            Listas.Col_song1.controls.append(tile)  # Agregar el ListTile a la columna Col_song1            
        page.update()
    else:
        show_error_dialog(page)

def open_spotify_link(song_id,page):
    spotify_link = f"http://open.spotify.com/track/{song_id}"
    page.launch_url(spotify_link)

def log(e, page):
    def on_login(e):
        if e.error:
            show_error_dialog(page)
        else:
            page.go('/playlist')
            get_user_info(page)
    page.login(provider)
    page.on_login = on_login
    page.update()
    

def gen_recom(e, page):
    access_token = token_manager.get_token()
    if access_token:
        Listas.Col_song2.clean()
        recomendaciones = AuthRequest.gen_recom_tracks(page.auth.token.token_type, token_manager.get_token())
        num_can = 1
        for cancion_info in recomendaciones:
            cancion_artista = cancion_info['cancion_artista']
            image_url = cancion_info['image_url']
            song_id = cancion_info['id']

            cancion, artista = cancion_artista.split(" - ", 1)
            # Crea el ListTile con la imagen de la canción
            tile = ft.ListTile(
                leading=ft.Image(src=image_url, width=50, height=350),  # La imagen de la canción
                title=ft.Text(cancion, size=20, font_family="Raleway"),  # El título será el nombre de la canción
                subtitle=ft.Text(artista, size=15, font_family="Raleway"),  # El subtítulo será el nombre del artista
                trailing=ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(
                            text="Escuchar",
                            on_click=lambda _, song_id=song_id: open_spotify_link(song_id,page),
                        ),
                    ],
                ),
                tooltip=f"{num_can}° Cancion recomendada"  # ¿De dónde viene num_can?
            )
            Listas.Col_song2.controls.append(tile)  # Agregar el ListTile a la lista de recomendaciones
        page.update()
    else:
        show_error_dialog(page)

# Método para asignar eventos a elementos UI
def events(page):
    buttons.btn_register.on_click = lambda e: log(e,page)
    buttons.btn_gen_recom.on_click = lambda e: gen_recom(e,page)
    buttons.btn_get_songs.on_click = lambda e: get_songs_user(e,page)
    buttons.btn_logout.on_click = lambda e: logout_button_click(e,page)
    

