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


def search_tracks_most_played(token_type, token):
    url = "https://api.spotify.com/v1/me/top/tracks"
    headers = get_auth_header(token)
    query = f"?limit=10"
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)

    canciones_artistas = []
    for item in json_result['items']:
        nombre_cancion = item['name']
        artistas = ', '.join(artist['name'] for artist in item['artists'])
        cancion_artista = f"{nombre_cancion} - {artistas}"
        
        if item.get('album') and item['album'].get('images'):
            image_url = item['album']['images'][0]['url']
        else:
            image_url = None
        cancion_id = item['id'] 
        canciones_artistas.append({
            'cancion_artista': cancion_artista,
            'image_url': image_url,
            'id': cancion_id
        })

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
        if track.get('album') and track['album'].get('images'):
            image_url = track['album']['images'][0]['url']
        else:
            image_url = None
        song_id = track['id']

        song_details.append({
            'cancion_artista': f"{song_name} - {artists}",
            'image_url': image_url,
            'id': song_id 
        })
    
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

def get_user_info(token_type, token, user_id):
    url = f"https://api.spotify.com/v1/users/{user_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    
    if result.status_code == 200:
        json_result = result.json()
        user_info = {
            'display_name': json_result.get('display_name', ''),
            'user_id': json_result.get('id', ''),
            'followers': json_result.get('followers', {}).get('total', 0),
        }
        images = json_result.get('images', [])
        images_list = []
        if images:
            images_list.append(images[0]['url'])
        
        user_info['images'] = images_list
        return [user_info]
    else:
        print(f"Failed to get user info. Status code: {result.status_code}")
        return None
