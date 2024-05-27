import spotipy
from spotipy.oauth2 import SpotifyOAuth
from credentials_manager import get_credentials

# Constants
FILE_PATH = '.cached_credentials'
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'playlist-read-private'
# Get credentials
client_id, client_secret, playlist_id = get_credentials()
# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

# Retrieve playlist information
results = sp.playlist(playlist_id)
tracks = results['tracks']['items']

# Extract track information and write to file
with open("playlist_tracks", 'w', encoding='utf-8', errors='replace') as f:
    for item in tracks:
        track = item['track']
        if track:
            artist_name = track['artists'][0]['name'] if track['artists'] else 'Unknown Artist'
            track_name = track['name'] if track['name'] else 'Unknown Track'
            f.write(f"{track_name} - {artist_name}\n")

print("Playlist exported successfully!")
