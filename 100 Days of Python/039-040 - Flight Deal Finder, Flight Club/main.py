from data_manager import DataManager
from flight_search import FlightSearch

# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.data_check()

for entry in sheet_data:
    entry['attributes']['iatacode'] = flight_search.iata_code(city=entry['attributes']['city'])

data_manager.data_insert(data=sheet_data)

sheet_data = data_manager.data_check()

for entry in sheet_data:
    location_iata = entry['attributes']['iatacode']
    location_city = entry['attributes']['city']
    low_price = int(entry['attributes']['lowestprice'])
    location_price = flight_search.low_prices(flight_data=entry)
    if low_price > location_price:
        print(f"{location_city} has a deal! Your low price is set at {low_price}, but I found a deal for {location_price}! Flying from {location_iata}!")

