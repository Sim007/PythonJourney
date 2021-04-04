# open-notify.org

import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print('json:')
print(json)
print('\n')

print('person json')
for person in json['people']: 
    print(person)
print('\n')

print('People currently in space:')
for person in json['people']: 
    print(person['name'])
print('\n')