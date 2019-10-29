import requests
import os
from datetime import datetime


key = os.environ.get('WEATHER_KEY')


def get_input(question):
    return input(question)


def make_api_call(city, country):
    query = {'q': city + ',' + country, 'units': 'imperial', 'appid': key}
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    data = requests.get(url, params=query).json()
    forecast = data['list']
    weather = forecast[0]
    description = weather['weather'][0]['description']
    temp = weather['main']['temp']
    cloudy = weather['clouds']['all']
    humidity = weather['main']['humidity']

    return description, temp, cloudy, humidity
