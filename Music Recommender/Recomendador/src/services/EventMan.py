# Este módulo contiene funciones y configuraciones para manejar la autenticación y la interacción con la API de Spotify, incluyendo la obtención de información del usuario, la gestión de tokens de acceso, la generación de recomendaciones, entre otras acciones.

# Importaciones necesarias
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
from components import Column_style as columna
from components import Avatar_style as avatar

from services import AuthRequest
from flet.auth import OAuthProvider
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración del proveedor OAuth para la autenticación con Spotify
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

# Clase para gestionar los tokens de acceso
class TokenManager:
    def __init__(self):
        self.access_token = None
    def set_token(self, access_token):
        self.access_token = access_token
    def get_token(self):
        return self.access_token
    def delete_token(self):
        self.access_token = None

class UserManager:
    def __init__(self):
        self.user_id = None
    def set_token(self, user_id):
        self.user_id=user_id
    def get_token(self):
        return self.user_id
    def delete_token(self):
        self.user_id = None
# Instancia del gestor de tokens
token_manager = TokenManager()
user_id = UserManager()

# Función para el clic del botón de cierre de sesión
def logout_button_click(e,page):
    avatar.user_state.bgcolor=ft.colors.RED
    # Cierra la ventana actual y abre la página de login
    token_manager.delete_token()
    page.client_storage.remove(page.auth.token.access_token)
    page.logout()
    page.go('/')

# Función para mostrar un diálogo de error en la interfaz de usuario
def show_error_dialog(page):
    page.go('/')
    alert_title = ft.Text("Error de inicio de sesión")
    alert_content = ft.Text("No se pudo ingresar. Inténtalo de nuevo más tarde.")
    error_dialog = ft.AlertDialog(title=alert_title, content=alert_content)
    page.dialog = error_dialog
    error_dialog.open = True
    page.update()

def show_error_previous(page):
    alert_title = ft.Text("Error, requiere accion previa")
    alert_content = ft.Text("Primero recupera tus canciones mas escuchadas")
    error_dialog = ft.AlertDialog(title=alert_title, content=alert_content)
    page.dialog = error_dialog
    error_dialog.open = True
    page.update()

# Función para verificar si el usuario está autenticado
def user_is_authenticated():
    access_token = token_manager.get_token()
    if access_token is not None:
        return True
    else:
        return False

# Función para obtener información del usuario
def get_user_info(page):
    user_info = AuthRequest.get_user_info(token_manager.get_token(),user_id.get_token())
    if user_info:
        user_data = user_info[0]
        Listas.list_user_info.controls.clear()
        images = user_data.get('images', [])
        if images and isinstance(images[0], str):
            avatar.user_image.foreground_image_url=images[0]
            avatar.user_state.bgcolor=ft.colors.GREEN
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

#Funcion para obtener canciones del usuario
def get_songs_user(e, page):
    access_token = token_manager.get_token()
    if access_token:
        columna.Col_song1.clean()
        artistas = AuthRequest.search_tracks_most_played(token_manager.get_token())
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
                            on_click=lambda _: open_spotify_link(song_id, page),
                        ),
                    ],
                ),
                tooltip=f"{num_can}° Cancion mas escuchada"
            )
            num_can += 1
            columna.Col_song1.controls.append(tile)  # Agregar el ListTile a la columna Col_song1            
        page.update()
    else:
        show_error_dialog(page)

# Función para abrir un enlace de Spotify
def open_spotify_link(song_id,page):
    spotify_link = f"http://open.spotify.com/track/{song_id}"
    page.launch_url(spotify_link)

# Función para manejar el inicio de sesión
def log(e, page):
    def on_login(e):
        if e.error:
            show_error_dialog(page)
        else:
            token_manager.set_token(page.auth.token.access_token)
            user_id.set_token(page.auth.user.id)
            page.go('/playlist')
            get_user_info(page)
    page.login(provider)
    page.on_login = on_login
    page.update()
    
# Función para generar recomendaciones de canciones
def gen_recom(e, page):
    if len(columna.Col_song1.controls) >0:
        recomendaciones = AuthRequest.gen_recom_tracks(token_manager.get_token())
        columna.Col_song2.clean()
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
            columna.Col_song2.controls.append(tile)  # Agregar el ListTile a la lista de recomendaciones
        page.update()
    else:
        show_error_previous(page)

# Método para asignar eventos a elementos de la interfaz de usuario
def events(page):
    buttons.btn_register.on_click = lambda e: log(e,page)
    buttons.btn_gen_recom.on_click = lambda e: gen_recom(e,page)
    buttons.btn_get_songs.on_click = lambda e: get_songs_user(e,page)
    buttons.btn_logout.on_click = lambda e: logout_button_click(e,page)
    

