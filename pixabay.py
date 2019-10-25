''' Testing out to call to pixabay API '''

import requests
import os
import random



key = os.environ.get('IMAGE_KEY')
image_search = input('What type of image do you want?')

#catergory_variable = input('What category are you looking for?')
colors_variable = input('Pick a color: ')

query = {'q': image_search, 'colors': colors_variable, 'key': key}



url = 'https://pixabay.com/api/'
data = requests.get(url, params=query).json()


hitsList = data['hits']

hit = random.choice(hitsList)

print(hit)