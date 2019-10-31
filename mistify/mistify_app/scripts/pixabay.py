import requests
import os
import random
from mistify_app.scripts import weather_forecast as weather


key = os.environ.get('IMAGE_KEY')


def get_image(weather):
    query = {'q': weather, 'key': key} #searches pixabay for image data by weather description
    url = 'https://pixabay.com/api/'
    data = requests.get(url, params=query).json()
    hitsList = data['hits'] #list of image data
    try:
        image = random.choice(hitsList) #randomly chooses image from results
    except IndexError:
        print('IndexError: Please check input')
        return 0
    return image['largeImageURL']
