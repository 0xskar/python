import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup

# Spotipy
auth_manager = SpotifyOAuth(scope='playlist-modify-public')
sp = spotipy.Spotify(auth_manager=auth_manager)

# Billboard top 100
URL = "https://www.billboard.com/charts/hot-100/"

while True:
    year = input("Which year to travel to? Format YYYY-MM-DD: ")
    if len(year) == 10 and year[4] == '-' and year[7] == '-':
        if year[:4].isdigit() and year[5:7].isdigit() and year[8:].isdigit():
            break
    else:
        print("Invalid format. Please try again.")

PLAYLIST_ID = input("Enter Your Playlist ID to add to: ")

r = requests.get(url=f"{URL}/{year}/")
top_100 = BeautifulSoup(r.text, "html.parser")
chart_results = top_100.find_all(class_="o-chart-results-list-row")

billboard_top_100 = []

for song in chart_results:
    song_title = song.h3.get_text().replace('\n', '').replace('\t', '')
    artist = song.h3.next_sibling.next_sibling.get_text().replace('\n', '').replace('\t', '')

    # create dictionary
    new_data = {
        "song": song_title,
        "artist": artist
    }
    billboard_top_100.append(new_data)

# get spotify URIs and add to list
spotify_song_uris = []
for song_num in range(len(billboard_top_100)):
    search_string = f"{billboard_top_100[song_num]['song']} {billboard_top_100[song_num]['artist']}"
    search_track = sp.search(search_string, type="track")
    if search_track['tracks']['items']:
        spotify_song_uris.append(search_track['tracks']['items'][0]['uri'])

print(spotify_song_uris)

sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=spotify_song_uris)
sp.playlist_change_details(playlist_id=PLAYLIST_ID, name=year)
