import requests
import os
import random
import weather_forecast as weather


key = os.environ.get('IMAGE_KEY')


def get_image(weather):
    query = {'q': weather, 'key': key}
    url = 'https://pixabay.com/api/'
    data = requests.get(url, params=query).json()
    hitsList = data['hits']
    image = random.choice(hitsList)
    return image['largeImageURL']