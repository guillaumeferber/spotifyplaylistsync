import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
file_path = '.cached_credentials';
client_id = ''
client_secret = ''
playlist_id = ''
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            info = line.strip().split(':')
            if len(info) == 2:
                if (info[0] == 'client_id'):
                    client_id = info[1]
                if (info[0] == 'client_secret'):
                    client_secret = info[1]
                if(info[0] == 'playlist_id'):
                    playlist_id = info[1]
            else:
                print("Could not retrieve credential")

# Input for client ID
client_id = client_id or input("Enter your Spotify Client ID: ")

# Input for client secret
client_secret = client_secret or input("Enter your Spotify Client Secret: ")

# Input for playlist ID
playlist_id = playlist_id or input("Enter the Spotify Playlist ID: ")


# Redirect URI for Spotify OAuth
redirect_uri = 'http://localhost:8888/callback'
scope = 'playlist-modify-public'
with open(file_path, 'w') as f:
    f.write(f"client_id:{client_id}\n")
    f.write(f"client_secret:{client_secret}\n")
    f.write(f"playlist_id:{playlist_id}\n")
# Authenticating with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# Function to read songs from file and add them to the playlist
def import_songs_from_file(filename, playlist_id):
    _filename = filename or "playlist_tracks.txt"
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
filename = input("Enter the filename containing songs: ")
if filename.strip():
    # Import songs from file and add them to the playlist
    import_songs_from_file(filename, playlist_id)
else:
    import_songs_from_file('playlist_tracks.txt', playlist_id)

print("Playlist updated successfully!")
