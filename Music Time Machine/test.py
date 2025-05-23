# https://github.com/AchintyaShah25/MusicalTimeMachine/blob/master/main.py

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

redirect = "https://example.com/callback"
S_CLIENT_ID = "a579b68ae9cf45a28ad5ed589ed4cf7d"
S_CLIENT_SECRET = "8d37d26eac1a4a7fa33de55648ea0c1e"
S_USER_ID = "antkn33"

user_date = "1987-06-01"
# user_date = input("What date Hot100 Would you like? YYYY-MM-DD\n")
year = user_date.split("-")[0]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_date}/")
response = response.text
soup = BeautifulSoup(response, "html.parser")
all_songs = [song_titles.getText().strip() for song_titles in soup.find_all(name="h3", class_="a-no-trucate")]
artists_name = [artists.getText().strip() for artists in soup.find_all(name="span", class_="a-no-trucate")]
all_artists = [singer for singer in artists_name]
song_artist = {}

for keys in all_songs:
    for value in artists_name:
        song_artist[keys] = value
        artists_name.remove(value)
        break
uri_li = []
spotify_credentials = SpotifyOAuth(client_id=S_CLIENT_ID, client_secret=S_CLIENT_SECRET,redirect_uri=redirect, scope="playlist-modify-private")
# access_token = spotify_credentials.get_cached_token()
# ACCESS_TOKEN = access_token["access_token"]
spotify = spotipy.Spotify(ACCESS_TOKEN)
for songs in all_songs:
    res = spotify.search(q=f"track:{songs} year:{year}", type="track")
    try:
        uri_li.append(res["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"'{songs}' not found")
playlist_name = f"{user_date} Billboard Hot 100 playlist"
desc = "Python generated top 100 songs of a particular day"
playlist = spotify.user_playlist_create(user=S_USER_ID, name=playlist_name, description=desc, public=False)
playlist_id = playlist["id"]
spotify.user_playlist_add_tracks(user=S_USER_ID, playlist_id=playlist_id,tracks=uri_li)