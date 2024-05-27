# Table of Contents

- [Spotify Playlist Exporter](#spotify-playlist-exporter)
- [Spotify Playlist Importer](#spotify-playlist-importer)

# Spotify Playlist Exporter

This tool allows you to export the songs from a specific Spotify playlist to a text file.

## Prerequisites

- Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- A Spotify account to access your playlists.

## Installing Dependencies

1. Open a command prompt or terminal.
2. Use the following command to install the `spotipy` library:
   ```
   pip install spotipy
   ```

## Configuring Spotify Application

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create a new application.
2. Note down your `Client ID` and `Client Secret`.
3. In your application settings, add `http://localhost:8888/callback` as the Redirect URI.

## Using the Python Script

1. Download the Python script `export_playlist.py` from this repository.
2. Open the script in a text editor and replace the following values:
   - `YOUR_CLIENT_ID`: Your Spotify client ID.
   - `YOUR_CLIENT_SECRET`: Your Spotify client secret.
   - `YOUR_PLAYLIST_ID`: The ID of the Spotify playlist you want to export.
3. Save the changes.

## Running the Script

1. Open a command prompt or terminal in the directory containing the `export_playlist.py` script.
2. Use the following command to run the script:
   ```
   python export_playlist.py
   ```
3. Follow the on-screen instructions to authorize the application to access your Spotify playlists.
4. Once authorized, the script will export the list of songs to a file named `playlist_tracks.txt`.

# Spotify Playlist Importer

This script allows you to import a list of tracks into an existing Spotify playlist.

## Prerequisites

1. Python 3.6 or later.
2. `requests` library installed.
3. A Spotify Premium account.
4. A Spotify access token with appropriate permissions (`playlist-modify-public` and/or `playlist-modify-private`).

## Installation

Before getting started, you need to install the `requests` library if it's not already installed:

```bash
pip install requests
```
## Configuration
You need to provide your own Spotify API credentials in the script. Here are the variables to configure:

- `client_id`: Your Spotify client ID.
- `client_secret`: Your Spotify client secret.
- `playlist_id`: The ID of the playlist where you want to add the tracks.
## Usage
To run the script, use the following command in your terminal:


```
python spotify_importer.py
```

You will be prompted to enter the titles of the tracks you want to add to the playlist. These titles should be formatted as "Track Title - Artist Name".
## Contributions
Contributions to this project are welcome. You can propose enhancements or fixes by submitting a pull request.

## License
This project is distributed under the MIT License. See the LICENSE file for more details.