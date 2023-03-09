from data_manager import DataManager
from flight_search import FlightSearch
#This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.sheet_data_check()
for entry in sheet_data:
    if entry['iataCode'] == "":
        entry['iataCode'] = flight_search.flightsearch(iatacode=entry['city'])

data_manager.sheet_data_insert(data=sheet_data)

