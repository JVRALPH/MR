import os  # Importa el módulo 'os', que proporciona funcionalidades para interactuar con el sistema operativo.
import flet as ft  # Importa la biblioteca 'flet' como 'ft'.
import requests
from flet.auth import OAuthProvider  # Importa la clase 'OAuthProvider' desde el módulo 'auth' de 'flet'.

def main(page: ft.Page):
    # Crea una instancia de OAuthProvider con los detalles de autenticación de Spotify.
    provider = OAuthProvider(
        client_id="584e8f3925884083861f2dcdb5216bdc",
        client_secret="ed7182da377449b59615aa8e49281e35",
        redirect_url="http://localhost:8550/api/oauth/redirect",
        authorization_endpoint="https://accounts.spotify.com/authorize?",
        token_endpoint="https://accounts.spotify.com/api/token",

        user_scopes=["user-read-private"],
    )

    # Función que se ejecuta cuando se hace clic en el botón de inicio de sesión.
    def login_click(e):
        page.login(provider)

    # Función que se ejecuta cuando se hace clic en el botón de cierre de sesión.
    def logout_button_click(e):
        page.logout()

    # Función que se ejecuta después de que se complete el proceso de inicio de sesión.
    def on_login(e):
        if e.error:
            raise Exception(e.error)
        print("User ID:", page.login.auth.token)

    # Asigna la función 'on_login' como el manejador de eventos para el evento de inicio de sesión.
    page.on_login = on_login

    # Agrega dos botones a la interfaz de usuario, uno para iniciar sesión y otro para cerrar sesión.
    page.add(
        ft.ElevatedButton("Login with Spotify", on_click=login_click),
        ft.ElevatedButton("Sign out", on_click=logout_button_click),
    )

# Crea una aplicación web usando 'flet', con el objetivo (target) de la función 'main',
# usando el puerto 8550 y mostrando la interfaz en un navegador web.
ft.app(target=main, port=8550, view=ft.WEB_BROWSER)
