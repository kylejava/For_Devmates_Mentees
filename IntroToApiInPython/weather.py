import json
import requests
from pprint import pprint
city = input("Enter a city name: ")
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid='YOUR API KEY'&units=metric'.format(city)

data = requests.get(url)
results = data.json()

#pprint(results) This line of code prints out the JSON data in a more cleaner way

print("The weather in " + results['name'] + " is " + str(results['main']['temp']) + " Celcius.")
