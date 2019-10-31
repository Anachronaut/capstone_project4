import unittest
from unittest import TestCase
from unittest.mock import patch, call

import main
import weather_forecast
import spotify
import pixabay
import os
import random
import requests
imgkey = os.environ.get('IMAGE_KEY')
weatherkey = os.environ.get('WEATHER_KEY')

class TestProgram(TestCase):




    # Test Pixabay API
    @patch('pixabay.get_image')
    def test_get_image(self, mock_weather): #tests pixabay input for zero results
        mock_weather = 'dsfafafsa'
        query = {'q': mock_weather, 'key': imgkey}
        url = 'https://pixabay.com/api/'
        data = requests.get(url, params=query).json()
        hitsList = data['hits']
        try:
            image = random.choice(hitsList)
        except IndexError:
            print('IndexError: Please check input')
            return 0
        assert (image != None)

    # Test Weather API
    @patch('weather_forecast.make_api_call')
    def test_make_api_call_country(self, mock_country): #tests weather api for invalid country code
        mock_city = 'Minneapolis'
        mock_country = 'KK'
        query = {'q': mock_city + ',' + mock_country, 'units': 'imperial', 'appid': weatherkey}
        url = 'https://api.openweathermap.org/data/2.5/forecast'
        try:
            data = requests.get(url, params=query).json()
            forecast = data['list']
        except KeyError:
            print(f'KeyError: Please check city name and country code in {query}')
            return 'Error! Please check city name and country code.', 0, 0, 0
        weather = forecast[0]
        assert (weather != None)

    @patch('weather_forecast.make_api_call')
    def test_make_api_call_city(self, mock_city): #tests weather api for invalid city name
        mock_city = 'asdfsafasd'
        mock_country = 'US'
        query = {'q': mock_city + ',' + mock_country, 'units': 'imperial', 'appid': weatherkey}
        url = 'https://api.openweathermap.org/data/2.5/forecast'
        try:
            data = requests.get(url, params=query).json()
            forecast = data['list']
        except KeyError:
            print(f'KeyError: Please check city name and country code in {query}')
            return 'Error! Please check city name and country code.', 0, 0, 0
        weather = forecast[0]
        assert (weather != None)

    @patch('spotify.get_weather_song')
    def test_get_weather_song(self, spotify): #tests spotify api for invalid playlist query
            searchResults = spotify.search(q=mock_query, limit=50, type='playlist')
            try:
                playlist = random.choice(searchResults['playlists']['items'])
            except IndexError:
                print('IndexError: Please check input')
            playlistURIs = []
            playlistURIs.append(playlist['uri'])
            return playlistURIs[0]
