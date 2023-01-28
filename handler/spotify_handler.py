import spotipy
import spotipy.oauth2 as oauth2

from config import config

USERNAME = config.SPOTIFY_USERNAME
SCOPE = config.SPOTIFY_SCOPE
CLIENT_ID = config.SPOTIFY_CLIENT_ID
CLIENT_SECRET = config.SPOTIFY_CLIENT_SECRET
PLAYLIST_ID = config.SPOTIFY_PLAYLIST_ID

auth_manager = oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
token = auth_manager.get_access_token()
# print(token)
sp = spotipy.Spotify(auth=token)


def get_playlist_items():
    results = sp.playlist_items(PLAYLIST_ID, fields="items.track", limit=100, offset=0, market='VN')
    # print(results)
    tracks = []
    for song in results["items"]:
        # print(track)
        # print(type(track))
        track = {
            'name': song['track']['name'],
            'spotify': song['track']['external_urls']['spotify'],
            'artists': song['track']['artists'][0]['name']
        }
        tracks.append(track)
    return tracks


# print(get_playlist_items())
