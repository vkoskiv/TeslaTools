
## TeslaTools - Simple tools for probing the Tesla Motors API.

## Requirements:

- Python3
- requests (pip3 install requests)

## Usage:

`./getToken.py <Your Tesla account email> <Your Tesla account password>`

This script will request a new token you can use for subsequent requests.  It will also store it in token.txt along with other useful info


`./decoder.py <Your authentication token (acquire with getToken.py)>`

This script will retrieve a list of your vehicles and decode the feature codes to a readable format.

## Security:

You should audit these scripts before providing your Tesla credentials.

## TODO:

- `getToken.py` should refresh the token if it's outdated automatically.
- New tools should be added.


