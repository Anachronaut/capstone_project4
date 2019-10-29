import requests
import os
import random
import weather_forecast as weather
import webbrowser


key = os.environ.get('IMAGE_KEY')


def get_image(weather):
    # Get image determined by the weather condition
    query = {'q': weather, 'key': key}
    url = 'https://pixabay.com/api/'
    data = requests.get(url, params=query).json()
    hitsList = data['hits']
    image = random.choice(hitsList)
    return image



def display_image(image):
    # Displays image in browser
    webbrowser.open(image.url)