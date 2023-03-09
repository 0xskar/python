import requests
from globals import *
from datetime import datetime, timedelta

class FlightSearch:
    def __init__(self):
        self.headers = TEQUILA_HEADERS
        self.api_key = TEQUILA_FLIGHT_SEARCH_API_KEY
        self.endpoint = TEQUILA_ENDPOINT
        self.fly_from = LOCAL_IATACODE

    def iata_code(self, city):
        """Search through KIWI API with City and return IATI Code"""
        params = {
            "term": city,
            "locale": "en-US",
            "location_types": "airport",
            "limit": "1",
            "active_only": "true"
        }
        r = requests.get(url=f"{self.endpoint}/locations/query", headers=self.headers, params=params)
        flightsearch_data = r.json()
        flight_iata_code = flightsearch_data['locations'][0]['code']
        return flight_iata_code

    def low_prices(self, flight_data):
        """Search through KIWI API with City and return Lowest Price"""
        # API FORMAT: https://api.tequila.kiwi.com/v2/search
        # ?fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021
        tomorrow = datetime.today() + timedelta(days=1)
        tomorrow = tomorrow.strftime("%d/%m/%Y")
        six_months = datetime.today() + timedelta(days=6*30)
        six_months = six_months.strftime("%d/%m/%Y")
        params = {
            "fly_from": self.fly_from,
            "fly_to": flight_data['attributes']['iatacode'],
            "dateFrom": tomorrow,
            "dateTo": six_months,
            "curr": "CAD"
        }
        r = requests.get(url=f"{TEQUILA_ENDPOINT}/search", headers=self.headers, params=params)
        data = r.json()["data"][0]
        return data['price'], data['deep_link']
