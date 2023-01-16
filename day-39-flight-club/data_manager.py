import requests
from pprint import pprint

header = {
    'Authorization': 'basic amR1bmdhbzE1OkowaG5taWd1ZWwq'
}
ENDPOINT = 'https://api.sheety.co/153c9b4f1befdcd938fd34b4df79bed6/flightDeals/prices'


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # self.city = None
        # self.iata_code = None
        # self.lowest_price = None
        self.destination_data = None

    def get_destination_data(self):
        response = requests.get(ENDPOINT, headers=header)
        response.raise_for_status()
        data = response.json()['prices']
        self.destination_data = data
        return data

    def update_destionation_data(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode'],
                }
            }
            response = requests.put(
                f"{ENDPOINT}/{city['id']}",
                headers=header,
                json=new_data)
            print(response.text)