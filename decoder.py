#!/usr/local/bin/python3

import json
import sys
import requests

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <Your authentication token (acquire with getToken.py)>")
    exit(-1)

authheader = "Bearer " + sys.argv[1]
url = "https://owner-api.teslamotors.com/api/1/vehicles"
headers = {
        'User-Agent': 'vkoskiv-tesladecoder',
        'Authorization': authheader}

data = requests.get(url, headers=headers)

# data = sys.stdin.read()

response = json.loads(data.text)

filename = 'features.json'

with open(filename) as f:
    feats = json.load(f)

cars = response["response"]

for car in cars:
    print(car["display_name"] + " (" + car["vin"] + ")",end=":\n")
    opts = car["option_codes"].split(',')
    for opt in opts:
        print("    ",end="")
        print(opt, end="")
        if len(opt) == 4:
            print("  = ", end="")
        if len(opt) == 5:
            print(" = ", end="")
        for obj in feats:
            if obj["code"] == opt:
                title = obj["title"]
        if not title:
            print("?")
        else:
            print(title)
