import requests
import os
from datetime import datetime

key = os.environ.get('WEATHER_KEY')

city = input('Enter city name: ')
country = input('Enter country code: ')

query = {'q': city+','+country, 'units': 'imperial', 'appid': key}

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
