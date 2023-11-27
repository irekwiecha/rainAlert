import json
import requests

# import private data
with open('priv.json') as f:
    priv = json.load(f)
    APIkey = priv["APIkey"]

