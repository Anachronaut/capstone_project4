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
weather_list = []


for forecast in forecast_items:
    timestamp = forecast['dt']
    date = datetime.fromtimestamp(timestamp) #Leaving time as UTC as you can enter global cities
    temp = forecast['main']['temp']
    wind_speed = forecast['wind']['speed']
    desc = forecast['weather'][0]['description']
    print(f'at {date}: Weather is: {desc}, Temperature is: {temp}°F, Wind Speed is: {wind_speed} mph')
