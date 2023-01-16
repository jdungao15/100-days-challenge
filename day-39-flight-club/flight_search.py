import requests

header = {
    'Content-Type': 'application/json',
    "apikey": 'WTiw1n3xxv-jS-t9bDZkkcduLFqrUZZN'
}
ENDPOINT = 'https://api.tequila.kiwi.com/v2/search'


class FlightSearch:


    def get_destination_code(self, city_name):
        code = "Testing"
        return code
