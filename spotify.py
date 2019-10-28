import os
import spotipy
import webbrowser
import spotipy.util as util
import json
from json.decoder import JSONDecodeError
import random


def get_username():
    # My user id: 1270957563
    return input("What is your Spotify ID?: ")



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
    searchResults = spotify.search(q=query, limit=50, type='track')

    # Get track details for searchResult
    track = searchResults['tracks']['items']

    trackURIs = []
    for t in track:
        trackURIs.append(t['uri'])
    
    # Plays track on appropriate device
    spotify.start_playback(device_id=deviceID, uris=trackURIs, 
                            offset= {"position": random.randint(0, len(track))})



def display_image(imageURL):
    # Displays Pixabay art in browser
    webbrowser.open(imageURL)
    pass