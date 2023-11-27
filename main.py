import json

import requests
from icecream import ic

ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

# import private data
with open('priv.json') as f:
    priv = json.load(f)
    APIkey = priv["APIkey"]
    lat = priv["lat"]
    lon = priv["lon"]

parameters = {
    "lat": lat,
    "lon": lon,
    "appid": APIkey,
    "units": "metric"
}

resp = requests.get(ENDPOINT, params=parameters)
resp.raise_for_status()
data = resp.json()
ic(data)
