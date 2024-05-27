import spotipy
from spotipy.oauth2 import SpotifyOAuth
from credentials_manager import get_credentials
# Constants
FILE_PATH = '.cached_credentials'
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'playlist-modify-public'
# Get credentials
client_id, client_secret, playlist_id = get_credentials()
# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

# Function to read songs from file and add them to the playlist
def import_songs_from_file(filename, playlist_id):
    _filename = filename or "playlist_tracks"
    with open(_filename, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            song_info = line.strip().split(' - ')
            if len(song_info) == 2:
                track_name, artist_name = song_info
                results = sp.search(q=f"track:{track_name} artist:{artist_name}", type='track')
                if results['tracks']['items']:
                    track_uri = results['tracks']['items'][0]['uri']
                    sp.playlist_add_items(playlist_id, [track_uri])
                    print(f"Added {track_name} by {artist_name} to the playlist.")
                else:
                    print(f"Could not find {track_name} by {artist_name}.")

# Input for filename containing songs
filename = input("Enter the filename containing songs: ").strip() or "playlist_tracks"

# Import songs from file and add them to the playlist
import_songs_from_file(filename, playlist_id)

print("Playlist updated successfully!")
