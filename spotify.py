import os
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError


scope = ('user-read-private ' +                 # Accesses user subscription details
        'user-read-playback-state ' +           # Reads currently playing track
        'user-modify-playback-state')           # Controls playback


def main():
    username = get_username()                   # get username
    token = erase_cache(username, scope)        # get token

    spotify = spotipy.Spotify(auth=token)       # Create Spotify object

    deviceID = get_devices(spotify)             # Make sure Spotify is open on a device


    # Main menu loop
    while True:
        main_menu()
        choice = input('Your choice: ')

        if choice == '0':
            searchQuery = get_weather('What is the weather?: ')
            get_weather_song(searchQuery, spotify, deviceID)    # Search for the artist
        elif choice == '1':
            break                                               # End the program



def get_username():
    # My user id: 1270957563
    return input("What is your Spotify ID?: ")



def erase_cache(user, scope):
    # Erase cache and prompt for user permission
    try:
        return util.prompt_for_user_token(user, scope)
    except (AttributeError, JSONDecodeError):
        os.remove(f'.cache-{user}')
        return util.prompt_for_user_token(user, scope)



def get_weather(question):
    return input(question)  # Replace the weather description from the weather API



def main_menu():
    # Main Menu
    print()
    print('>>> Welcome!!!!!!!!!!!!!!!!!!!!')
    print()
    print('0 - Get the weather')
    print('1 - exit')
    print()
    pass



def get_devices(spotify):
    # Get current device (smartphone, desktop, etc)
    devices = spotify.devices()
    return devices['devices'][0]['id']



def get_weather_song(query, spotify, deviceID):
    # Basically this searches for tracks that contain whatever the weather description is in it.
    # It returns the first result (change limit parameter to return more results)
    searchResults = spotify.search(q=query, limit=1, type='track')          # TODO: Change to playlist

    # Get track details for searchResult
    track = searchResults['tracks']['items'][0]

    trackID = track['id']                               # Track attributes
    trackKey = track['key']                             #
    trackMode = track['mode']                           #
    trackTimeSignature = track['time_signature']        #
    trackAcoustic = track['acousticness']               #
    trackInstrumentalness = track['instrumentalness']   #
    trackLiveness = track['liveness']                   #
    trackLoudness = track['loudness']                   #
    trackSpeechiness = track['speechiness']             #
    trackTempo = track['tempo']                         # 
    trackValence = track['valence']                     #
    trackDance = track['danceability']                  #
    trackEnergy = track['energy']                       #

    trackURIs = []
    trackURIs.append(track['uri'])
    spotify.start_playback(device_id=deviceID, uris=trackURIs)    # Plays track on appropriate device

    # Displays album art in browser
    webbrowser.open(track['album']['images'][0]['url'])           # TODO: Replace album art with PixaBay API request

    

main()