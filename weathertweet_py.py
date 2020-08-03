
# Dependencies
import tweepy
import time
import json
import os
import random
import requests as req
import datetime

is_heroku = False
if 'IS_HEROKU' in os.environ:
    is_heroku = True

if is_heroku:
    consumer_key = os.environ.get('consumer_key')
    consumer_secret = os.environ.get('consumer_secret')
    access_token = os.environ.get('access_token')
    access_token_secret = os.environ.get('access_token_secret')
    weather_api_key = os.environ.get('weather_api_key')
else:
    from config import consumer_key, consumer_secret, access_token, access_token_secret, weather_api_key

# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret


def WeatherTweet():

    # Construct a Query URL for the OpenWeatherMap
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    city = 'Washington, D.C.'
    units = 'imperial'
    query_url = (f'{url}appid={weather_api_key}&q={city}&units={units}')

    # Perform the API call to get the weather
    weather_response = req.get(query_url)
    weather_json = weather_response.json()
    print(weather_json)

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the weather
    api.update_status(
        "TK - Weather in DC " +\
        (datetime.datetime.now().strftime("%I:%M %p") + " " +\
         str(weather_json["main"]["temp"])+"F"))

    # Print success message
    print("Tweeted successfully!")



while(True):
    WeatherTweet()
    time.sleep(60)


