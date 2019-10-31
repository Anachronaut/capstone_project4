import requests
import os
from datetime import datetime


key = os.environ.get('WEATHER_KEY')


def get_input(question):
    return input(question)


def make_api_call(city, country):
    query = {'q': city + ',' + country, 'units': 'imperial', 'appid': key}  #searches openweathermap by city & country
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    try:
        data = requests.get(url, params=query).json()
        forecast = data['list'] #list of weather data
    except KeyError:
        print(f'KeyError: Please check city name and country code in {query}')
        return 'Error! Please check city name and country code.', 0, 0, 0
    weather = forecast[0] #returns current day
    description = weather['weather'][0]['description']
    temp = weather['main']['temp']
    cloudy = weather['clouds']['all']
    humidity = weather['main']['humidity']
    description = description.capitalize()

    return description, temp, cloudy, humidity
