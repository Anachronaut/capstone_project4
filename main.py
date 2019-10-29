import spotipy
import database as db
import pixabay as pixabay
import spotify as spotify
from classes import PixabayImage
from classes import SpotifyTrack
import weather_forecast as weather



def main():
    # Display banner when program starts
    banner()

    # OpenWeather API
    city = weather.get_input('Enter city name: ')                           # Get city to check weather in
    country = weather.get_input('Enter country code: ')                     # Get 2-digit country code
    weatherDescription = weather.make_api_call(city, country)               # Make call to OpenWeather API


    # Spotify API
    username = spotify.get_username()                                       # Get user's Spotify ID
    scope = spotify.get_scope()                                             # Get scope for how the program can interact with user's profile
    token = spotify.erase_cache(username, scope)                            # Get token for authorization
    spotifyObject = spotify.spotipy.Spotify(auth=token)                     # Create a Spotify object
    deviceID = spotify.get_devices(spotifyObject)                           # Get ID for user's device currently using Spotify

    track = spotify.get_track(weatherDescription, spotifyObject)            # Gets a track from Spotify
    trackObject = get_spotify_track(                                        # Create an object with track attributes
        track['id'], 
        track['artists'][0]['name'], 
        track['name'], 
        track['uri'])
    spotify.play_track(trackObject, spotifyObject, deviceID)                # Plays track on appropriate device


    # Pixabay API
    image = pixabay.get_image(weatherDescription)                           # Get image  based on weatherDescription
    imageObject = get_pixabay_image(                                        # Create an object with image attributes
        image['id'],
        image['largeImageURL']
    )
    pixabay.display_image(imageObject)                                      # Dispay image in browser


    # Main menu loop
    while True:
        main_menu()
        choice = input('Your choice: ')

        if choice == '1':                                                   # Get another song based on the weather
            track = spotify.get_track(weatherDescription, spotifyObject)
            trackObject = get_spotify_track(
                track['id'],
                track['artists'][0]['name'],
                track['name'],
                track['uri'])
            spotify.play_track(trackObject, spotifyObject, deviceID)

            image = pixabay.get_image(weatherDescription)
            imageObject = get_pixabay_image(
                image['id'],
                image['largeImageURL']
            )
            pixabay.display_image(imageObject)
        elif choice == '2':                                                 # save song to database
            db.add_track(trackObject, imageObject)
        elif choice == '3':                                                 # view songs in database
            db.display_all()
        elif choice == '4':                                                 # get song from database
            pass
        elif choice == '0':
            end()
            break  



def banner():
    print()
    print('>>> Welcome!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('>>> MAKE SURE YOU HAVE SPOTIFY RUNNING FIRST!')
    print()



def main_menu():
    # Continue
    print()
    print('1 - Get a new song')
    print('2 - Boomark song')
    print('3 - View bookmarked songs')
    print('4 - Retrieve a previously bookmarked song')
    print('0 - exit')
    print()



def end():
    print()
    print('Goodbye!')



def get_spotify_track(i, a, n, u):
    # Create object for Spotify track
    return SpotifyTrack(i, a, n, u)


def get_pixabay_image(i, u):
    # Create object for Pixabay image
    return PixabayImage(i, u)



main()