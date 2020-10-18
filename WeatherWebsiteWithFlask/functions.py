import requests
import json
from keys import *
def getWeather(city):
    url = ('http://api.openweathermap.org/data/2.5/weather?q={}&appid='+ api_key+'&units=metric').format(city)
    data = requests.get(url)
    data = data.json()
    temp = data['main']['temp']
    return temp
