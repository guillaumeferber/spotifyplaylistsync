# credentials_manager.py

import os

CREDENTIALS_FILE = '.cached_credentials'

def load_credentials():
    credentials = {}
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                key, sep, value = line.strip().partition(':')
                if sep and value:
                    credentials[key] = value
                else:
                    print("Could not retrieve credential from line:", line)
    return credentials

def save_credentials(client_id, client_secret, playlist_id):
    with open(CREDENTIALS_FILE, 'w', encoding='utf-8') as f:
        f.write(f"client_id:{client_id}\n")
        f.write(f"client_secret:{client_secret}\n")
        f.write(f"playlist_id:{playlist_id}\n")

def get_credentials():
    credentials = load_credentials()
    client_id = credentials.get('client_id') or input("Enter your Spotify Client ID: ")
    client_secret = credentials.get('client_secret') or input("Enter your Spotify Client Secret: ")
    playlist_id = credentials.get('playlist_id') or input("Enter the Spotify Playlist ID: ")

    save_credentials(client_id, client_secret, playlist_id)
    return client_id, client_secret, playlist_id
