import requests

# Use of API keys calling the weather in a given city
# Gather user input of what city to check
city = input('Please enter a city to check the weather for: ')

# API call with the city input being concatenated
url = 'http://api.weatherapi.com/v1/current.json?key=8efe6727efa04c60998160120241912&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()

# Gets the nested JSON directories and pastes them to the console
temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print("Today's weather in", city, "is", description, "and", temp)