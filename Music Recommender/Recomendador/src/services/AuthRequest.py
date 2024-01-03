import os,json
import flet
from requests import post, get

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}
    
def search_artist_most_played(token_type,token):
    url="https://api.spotify.com/v1/me/top/artists"
    headers = get_auth_header(token)
    query = f"?&limit=10"
    query_url = url+query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    artistas = json_result['items']
    nombres_artistas = [artista['name'] for artista in artistas]
    
    return nombres_artistas

def search_tracks_most_played(token_type,token):
    url="https://api.spotify.com/v1/me/top/tracks"
    headers = get_auth_header(token)
    query = f"?&limit=10"
    query_url = url+query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    """
    nombres_canciones = [item['name'] for item in json_result['items']]
    for nombre in nombres_canciones:
        print(nombre)
    """
    canciones_artistas = []
    for item in json_result['items']:
        nombre_cancion = item['name']
        artistas = ', '.join(artist['name'] for artist in item['artists'])
        cancion_artista = f"{nombre_cancion} - {artistas}"
        canciones_artistas.append(cancion_artista)

    for cancion_artista in canciones_artistas:
        print(cancion_artista)

def search_user_saved_tracks(token_type,token):
    url="https://api.spotify.com/v1/me/tracks"
    headers = get_auth_header(token)
    query = f"?&limit=10"
    query_url = url+query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    print(json_result)