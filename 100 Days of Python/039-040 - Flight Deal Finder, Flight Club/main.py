from data_manager import DataManager
from flight_search import FlightSearch
from globals import *

city_insert = input("Enter a new city to check: ")
city_price = input("Enter the new cities wanted price: ")

data_manager = DataManager()
data_manager.data_create(city=city_insert, lowprice=city_price)

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
    location_price, flight_link = flight_search.low_prices(flight_data=entry)
    if low_price > location_price:
        print(f"{location_city} has a deal! Your low price is set at ${low_price} CAD, but I found a deal for ${location_price} CAD! Flying from {LOCAL_IATACODE} to {location_iata}! See {flight_link} to book")

