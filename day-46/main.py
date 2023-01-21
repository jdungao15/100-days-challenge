import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint as pp

CLIENT_ID = 'bba42b14b05144eabb2b4d61017235ba'
CLIENT_SECRET = '64c1c57b9a2448918f2def22591f13b5'

user_input = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
URL = f"https://www.billboard.com/charts/hot-100/{user_input}"
year = user_input[:4]
response = requests.get(URL)
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
songs_tag = soup.select(selector='li>h3#title-of-a-story')
song_title_list = [song.text.strip() for song in songs_tag]
# author_tag = soup.select(selector='li>h3#title-of-a-story+span')
# song_author_list = [song.text.strip() for song in author_tag]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="https://example.com/",
    cache_path=".cache",
    scope="playlist-modify"))

user_id = sp.current_user()["id"]
songs_id = []

for song in song_title_list:
    query = f"track:{song} year:{year}"
    results = sp.search(query, type="track")
    try:
        # track = results['tracks']['items'][0]['album']['artists'][0]['id']
        track = results['tracks']['items'][0]['uri']
    except IndexError:
        continue
        print("Track not found")
    else:
        songs_id.append(track)

# !-------------------DEBUGGING PURPOSES ----------------
# results = sp.search('track: Perfect year:2018')
# track = results['tracks']['items'][0]['album']['artists'][0]
# print(track)

name = f"top 100 billboard of year {year}"
description = f"list of 100 songs from billboard"
playlist = sp.user_playlist_create(user_id, name=name, public=True, description=description)
playlist_id = playlist['id']
print(playlist_id)

sp.playlist_add_items(playlist_id=playlist_id, items=songs_id)
