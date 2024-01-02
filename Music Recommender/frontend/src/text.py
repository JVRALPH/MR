import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

# Configura tus credenciales de la API de Spotify
client_id = '584e8f3925884083861f2dcdb5216bdc'
client_secret = 'ed7182da377449b59615aa8e49281e35'
redirect_uri = 'http://127.0.0.1:61905/playlist'  
# Debes añadir esta URI en la configuración de tu aplicación en el panel de desarrolladores de Spotify

# Indica los permisos que necesitas (en este caso, obtener las canciones más escuchadas)
scope = 'user-top-read'

# Indica el usuario de Spotify del que quieres obtener la información (su ID de usuario)
username = 'JVRALPH'

# Autenticación con la API de Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Obtener el token de acceso (esto abrirá una página en tu navegador para la autenticación)
token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)
    # Obtener las canciones más escuchadas del usuario (aquí se muestran las 10 primeras)
    top_tracks = sp.current_user_top_tracks(limit=10, offset=0, time_range='short_term')  # Puedes ajustar el rango de tiempo

    # Mostrar información sobre las canciones obtenidas
    print("Canciones más escuchadas:")
    for i, track in enumerate(top_tracks['items'], start=1):
        print(f"{i}. {track['name']} - {', '.join([artist['name'] for artist in track['artists']])}")
else:
    print("No se pudo obtener el token de acceso.")
