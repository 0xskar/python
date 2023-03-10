from globals import *
import requests


class DataManager:
    """This class is responsible for talking to the Google Sheet..Well it was until i realised Sheety was not a good
    deal at all..."""
    def __init__(self):
        self.auth_header = STRAPI_HEADERS

    def data_check(self):
        """Get all cities from stapi flight_deals"""
        r = requests.get(url=STRAPI_URL_ENDPOINT, headers=self.auth_header)
        spreadsheet_data = r.json()
        data = [location for location in spreadsheet_data['data']]
        return data

    def data_insert(self, data):
        """Insert data back into strapi"""
        # Put the data back
        for city in data:
            params = {
                "data": {
                    "city": city['attributes']['city'],
                    "iatacode": city['attributes']['iatacode'],
                    "lowestprice": city['attributes']['lowestprice']
                }
            }
            url = f"{STRAPI_URL_ENDPOINT}/{city['id']}"
            r = requests.put(url=url, headers=self.auth_header, json=params)

    def data_create(self, city, lowprice):
        params = {
            "data": {
                "city": city,
                "iatacode": "",
                "lowestprice": lowprice
            }
        }
        url = f"{STRAPI_URL_ENDPOINT}"
        r = requests.post(url=url, headers=self.auth_header, json=params)


