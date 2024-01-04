import os,json,random
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

    canciones_artistas = []
    for item in json_result['items']:
        nombre_cancion = item['name']
        artistas = ', '.join(artist['name'] for artist in item['artists'])
        cancion_artista = f"{nombre_cancion} - {artistas}"
        canciones_artistas.append(cancion_artista)
    return canciones_artistas

def search_user_saved_tracks(token_type,token):
    url="https://api.spotify.com/v1/me/tracks"
    headers = get_auth_header(token)
    query = f"?&limit=10"
    query_url = url+query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    print(json_result)

def gen_recom_tracks(token_type, token):
    headers = get_auth_header(token)
    url = "https://api.spotify.com/v1/recommendations"
    id_songs = get_track_seeds(token_type, token)
    query = f"?&limit=10&seed_tracks="
    query_url = url + query + id_songs
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    
    song_details = []
    for track in json_result['tracks']:
        song_name = track['name']
        artists = ', '.join(artist['name'] for artist in track['artists'])
        song_details.append(f"{song_name} - {artists}")
    
    return song_details



def get_track_seeds(token_type, token):
    url = "https://api.spotify.com/v1/me/top/tracks"
    headers = get_auth_header(token)
    query = f"?&limit=10"
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)

    track_ids = []
    for item in json_result['items']:
        track_id = item['id']
        track_ids.append(track_id)

    if len(track_ids) > 5:
        track_ids = random.sample(track_ids, 5)

    track_ids_str = ','.join(track_ids)
    return track_ids_str

