import os
import random
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError


def get_scope():
    return ('user-read-private ' +                  # Accesses user subscription details
            'user-read-playback-state ' +           # Reads currently playing track
            'user-modify-playback-state')           # Controls playback



def erase_cache(user, scope):
    # Erase cache and prompt for user permission
    try:
        return util.prompt_for_user_token(user, scope)
    except (AttributeError, JSONDecodeError):
        os.remove(f'.cache-{user}')



def get_devices(spotify):
    # Get current device (smartphone, desktop, etc)
    devices = spotify.devices()
    return devices['devices'][0]['id']



def get_weather_song(query, spotify, deviceID):
    # Basically this searches for tracks that contain whatever the weather description is in it.
    # It returns the first result (change limit parameter to return more results)
    searchResults = spotify.search(q=query, limit=50, type='playlist')

    # Get track details for searchResult; Maybe change this to the recommendations function, create a new playlist for the user?
    try:
        playlist = random.choice(searchResults['playlists']['items'])
    except IndexError:
        print('IndexError: Please check input')

    playlistURIs = []
    playlistURIs.append(playlist['uri'])
    #spotify.start_playback(device_id=deviceID, uris=trackURIs)    # Plays track on appropriate device
    return playlistURIs[0]
