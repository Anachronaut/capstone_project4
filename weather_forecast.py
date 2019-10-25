import requests
import os
from datetime import datetime


key = os.environ.get('WEATHER_KEY')


def get_city():
    city = input('Enter city name: ')


def get_country():
    country = input('Enter country code: ')


def get_input(question):
    return input(question)




query = {'q': get_city() + ',' + get_country(), 'units': 'imperial', 'appid': key}

url = 'https://api.openweathermap.org/data/2.5/forecast'
data = requests.get(url, params=query).json()
forecast_items = data['list']
weather = forecast_items[0]

timestamp = weather['dt']
date = datetime.fromtimestamp(timestamp) #Leaving time as UTC as you can enter global cities
temp = weather['main']['temp']
desc = weather['weather'][0]['description']
humidity = weather['main']['humidity']
cloudy = weather['clouds']['all']
print(f'at {date}: Weather is: {desc}, Temperature is: {temp}°F, Cloudiness at: {cloudy}, Humidity at: {humidity}')
