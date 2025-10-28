import json
import requests


pyyntö = "https://api.chucknorris.io/jokes/random"
try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(json_vastaus["value"])
except requests.exceptions.RequestException as e:
    print("Search couldn't be completed")