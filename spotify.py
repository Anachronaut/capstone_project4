import os
import random
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError


def get_username():
    # Gets User's Spotify ID
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



def get_track(query, spotify):
    # Searches Spotify for up to 50 tracks that includes the weather description
    # and return one track at random
    searchResults = spotify.search(q=query, limit=50, type='track')
    return searchResults['tracks']['items'][random.randint(0, len(searchResults)+1)]



def play_track(track, spotify, deviceID):
    trackURIs = []
    trackURIs.append(track.uri)
    
    # Plays track on appropriate device
    spotify.start_playback(device_id=deviceID, uris=trackURIs)