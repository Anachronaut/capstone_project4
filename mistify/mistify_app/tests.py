from django.test import TestCase

# Create your tests here.
import unittest
from unittest import TestCase
from unittest.mock import patch, call
import scripts
from scripts import main
from scripts import weather_forecast as weather_forecast
from scripts import spotify
from scripts import pixabay
#import database as db

import os
import random
imgkey = os.environ.get('IMAGE_KEY')
weatherkey = os.environ.get('WEATHER_KEY')

class TestProgram(TestCase):

    # Test Pixabay API
    @patch('pixabay.get_image')
    def test_get_image(self, mock_weather):
        mock_weather = snow
        example_api_response = {'q': mock_weather, 'key': imgkey}

        hitsList = data[example_api_response]
        image = random.choice(hitsList)
        assert (image != null)

    # Test Weather API
    @patch('weather_forecast.make_api_call')
    def test_api_call(self, mock_city, mock_country):
        mock_city = minneapolis
        mock_country = us
        example_api_response = query = {'q': mock_city + ',' + mock_country, 'units': 'imperial', 'appid': weatherkey}

        forecast = data[ example_api_response ]
        weather = forecast[0]

        assert (weather != null)


    # Test Spotify API

    # Test Weather to Spotify

    # Test Weather to Pixabay



    # Data base tests
