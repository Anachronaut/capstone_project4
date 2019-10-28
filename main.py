import spotipy
import spotify as spotify
import weather_forecast as weather
import pixabay as pixabay


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
    spotify.get_weather_song(weatherDescription, spotifyObject, deviceID)   # Make call to Spotify API

    # Pixabay API
    image = pixabay.get_image(weatherDescription)                           # Get image URL based on weatherDescription
    pixabay.display_image(image)                                            # Dispay image in browser


    # Main menu loop
    while True:
        main_menu()
        choice = input('Your choice: ')

        if choice == '0':
            # Get another song based on the weather
            spotify.get_weather_song(weatherDescription, spotifyObject, deviceID)
        elif choice == '1':
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
    print('0 - Get another song')
    print('1 - exit')
    print()



def end():
    print()
    print('Goodbye!')



main()