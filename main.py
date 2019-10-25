import spotipy
import spotify as spotify
import weather_forecast as weather
import pixabay as pixabay


def main():

    banner()

    # Weather
    city = weather.get_input('Enter city name: ')
    country = weather.get_input('Enter country code: ')
    weatherDescription = weather.make_api_call(city, country)

    # Spotify
    username = spotify.get_username()
    scope = spotify.get_scope()
    token = spotify.erase_cache(username, scope)
    spotifyObject = spotify.spotipy.Spotify(auth=token)
    deviceID = spotify.get_devices(spotifyObject)
    spotify.get_weather_song(weatherDescription, spotifyObject, deviceID)

    # Pixabay
    image = pixabay.get_image(weatherDescription)
    spotify.display_image(image)


    # Main menu loop
    while True:
        main_menu()
        choice = input('Your choice: ')

        if choice == '0':
            searchQuery = weatherDescription
            spotify.get_weather_song(searchQuery, spotifyObject, deviceID)
        elif choice == '1':
            break  



def main_menu():
    # Continue
    print()
    print('0 - Get another song')
    print('1 - exit')
    print()
    pass


def banner():
    print()
    print('>>> Welcome!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('>>> MAKE SURE YOU HAVE SPOTIFY RUNNING FIRST!')
    print()
    pass



main()