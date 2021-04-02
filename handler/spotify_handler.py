import json

import spotipy
import spotipy.oauth2 as oauth2

username = 'dhyxi2nynfg8ix3ddcmmhhl6u'
scope = 'user-library-read'
# scope = 'playlist-modify-public'

CLIENT_ID = 'db2735761229484685c1e719a8940998'
CLIENT_SECRET = 'e8cfb46db40c4b4ba684e49ac70a9084'

playlist_id = '3IhDh1G4c4JoqaDUQtxIdv'

auth_manager = oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
token = auth_manager.get_access_token()
print(token)
sp = spotipy.Spotify(auth=token)


def get_playlist_items():
    results = sp.playlist_items(playlist_id, fields="items.track", limit=100, offset=0, market='VN')
    # print(results)
    tracks = []
    for song in results["items"]:
        # print(track)
        # print(type(track))
        track = {
            'name': song['track']['name'],
            'spotify': song['track']['external_urls']['spotify']
        }
        tracks.append(track)
    return tracks


# print(get_playlist_items())
