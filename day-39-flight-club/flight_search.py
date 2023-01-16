import requests
from pprint import pprint

header = {
    'Content-Type': 'application/json',
    "apikey": 'WTiw1n3xxv-jS-t9bDZkkcduLFqrUZZN'
}
ENDPOINT = 'https://api.tequila.kiwi.com'

class FlightSearch:
    def get_destination_code(self, city_name):
        location_endpoint = f"{ENDPOINT}/locations/query"
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=header, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code