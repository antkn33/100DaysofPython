#
from bs4 import BeautifulSoup
import pprint 
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# Spotify user authentication
# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="a579b68ae9cf45a28ad5ed589ed4cf7d", client_secret="8d37d26eac1a4a7fa33de55648ea0c1e"))
# Spotify oauth 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="a579b68ae9cf45a28ad5ed589ed4cf7d",
                                                        client_secret="8d37d26eac1a4a7fa33de55648ea0c1e",
                                                        redirect_uri="https://example.com/callback",
                                                        scope="playlist-modify-private",
                                                        username="antkn33",
                                                        show_dialog=True,
                                                        cache_path="token.txt",))
# user = sp.current_user()
# user_id = user['id']
# print(user_id)

# Spotify test
# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

date = "1987-06-01"
# date = input("Select a date to view the Hot 100 Chart in this format: YYYY-MM-DD. ")

url = "https://www.billboard.com/charts/hot-100/" + date

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url, headers=headers)

chart = response.text

soup = BeautifulSoup(chart, "html.parser")
# (print(soup.prettify()))


song_list = soup.select("li ul li h3")
artist_list = soup.find_all(name='span', class_='u-max-width-330')

# print(song_list)

results = ([title.getText().strip() for title in song_list], [artist.getText().strip() for artist in artist_list])
print(results)


year = date.split("-")[0]
song_uri = []
for song in song_title:
  list = sp.search(q=f"track: {song} year:{year}", type="track", limit=1)
  pprint.pp(list["tracks"]["items"][0]["uri"])
  # song_uri.append(uri)
  # pprint.pp(list)

