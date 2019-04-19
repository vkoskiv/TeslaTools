#!/usr/local/bin/python3

import json
import sys
import requests
import os.path

if len(sys.argv) < 3:
    print("Usage: " + sys.argv[0] + " <Your Tesla account email> <Your Tesla account password>")
    exit(-1)

# Next check if we want to request a token, refresh it or just use the existing one
if os.path.isfile("token.txt"):
    with open("token.txt", "r") as tokenfile:
        check = json.load(tokenfile)
    print("You already have a token!")
    print("Your token is: " + check["access_token"])
    exit(0)

url = "https://owner-api.teslamotors.com/oauth/token"
headers = {'User-Agent': 'vkoskiv-tesladecoder'}

req = {}
req["grant_type"] = "password"
req["client_id"] = "81527cff06843c8634fdc09e8ac0abefb46ac849f38fe1e431c2ef2106796384"
req["client_secret"] = "c7257eb71a564034f9419ee651c7d0e5f7aa6bfbd18bafb5c5c033b093bb2fa3"
req["email"] = sys.argv[1]
req["password"] = sys.argv[2]

# print(json.dumps(req))
# exit(-1)
resp = requests.post(url, headers=headers, data=req)

respjson = json.loads(resp.text)

if 'error' in respjson:
    print("An error happened. Probably invalid credentials. Here's the full story from Tesla: ")
    print("\"{}\"".format(respjson["error_description"]))
    exit(-1)

if 'response' in respjson:
    if 'authorization_required_for_txid_``' in respjson["response"]:
        print("Invalid credentials. Probably.")
        exit(0)

if 'access_token' in respjson:
    print("Your new token is: {}".format(respjson["access_token"]))
    print("It will expire in {} days.".format((((respjson["expires_in"]/60)/60)/24)))
    print("It will also be saved in this directory as \'token.txt\'")
    print("You should keep a hold of this token and reuse it instead of requesting a new one for every use.")

    with open("token.txt", "w") as tokenfile:
        tokenfile.write(json.dumps(respjson))
