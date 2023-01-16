from flight_search import FlightSearch
from data_manager import DataManager
from pprint import  pprint
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to
# achieve the program requirements.


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()


#Check if sheetdata conatines any values for iataCode key.
if sheet_data[0]['iataCode'] == '':
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])
    print(f"sheet_data: \n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destionation_data()
