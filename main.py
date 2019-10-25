import spotify


def main():

    # Weather
    city = input('Enter city name: ')
    country = input('Enter country code: ')

    # Spotify
    username = spotify.get_username()
    scope = spotify.scope
    token = spotify.erase_cache(username, scope)
    spotifyObject = spotify.spotipy.Spotify(auth=token)
    deviceID = spotify.get_devices(spotifyObject)

    # Pixabay



main()