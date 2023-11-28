import json

import requests
from twilio.rest import Client

ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

# import private data
with open("priv.json") as f:
    priv = json.load(f)
    APIkey = priv["APIkey"]
    lat = priv["lat"]
    lon = priv["lon"]
    account_sid = priv["account_sid"]
    auth_token = priv["auth_token"]
    twilio_nr = priv["twilio_nr"]
    my_nr = priv["my_nr"]

parameters = {"lat": lat, "lon": lon, "appid": APIkey, "units": "metric", "cnt": 4}

resp = requests.get(ENDPOINT, params=parameters)
resp.raise_for_status()
weather_data = resp.json()["list"]

will_rain = False
for three_hour in weather_data:
    for data in three_hour["weather"]:
        if data["id"] < 700:
            will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=twilio_nr,
        body="Take an umbrella with you ☂. The precipitation is expected.",
        to=my_nr,
    )
