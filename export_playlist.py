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
scope = 'playlist-read-private'
with open(file_path, 'w') as f:
    f.write(f"client_id:{client_id}\n")
    f.write(f"client_secret:{client_secret}\n")
    f.write(f"playlist_id:{playlist_id}\n")
# Authenticating with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# Retrieving playlist information
results = sp.playlist(playlist_id)
tracks = results['tracks']['items']

# Extracting track information and writing to file
with open("playlist_tracks.txt", 'w', encoding='utf-8', errors='replace') as f:
    for item in tracks:
        track = item['track']
        if track is None:
            continue  # Passe au prochain item si track est None
        artist_name = track['artists'][0]['name'] if track['artists'] else 'Unknown Artist'
        track_name = track['name'] if track['name'] else 'Unknown Track'
        f.write(f"{track_name} - {artist_name}\n")

print("Playlist exported successfully!")