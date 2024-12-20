import requests

# Sample REST API Call to GET all of the people currently in space

response = requests.get('http://api.open-notify.org/astros.json')

# convert the responses to json
json = response.json()

print('The people currently in space are:')

# filter the responses to only display the people and their names, on a new line
for person in json['people']:
    print(person['name'])