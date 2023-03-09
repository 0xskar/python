from globals import *
import requests

# https://docs.google.com/spreadsheets/d/1vAbdwFtCkWplzDfSwHWJ4mohxhJS0SvAnXMmQg6dAKE

class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.auth_header = {
            "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
        }


    def sheet_data_check(self):
        """Get all cities from flight deals spreadsheet with empty  IATA code"""
        r = requests.get(url=SHEETY_API_ENDPOINT, headers=self.auth_header)
        spreadsheet_data = r.json()
        data = [location for location in spreadsheet_data['prices']]
        return data

    def sheet_data_insert(self, data):
        """Insert data back into spreadsheet"""
        for entry in data:
            sheet_data = {
                "price": entry
            }
            r = requests.put(url=f"{SHEETY_API_ENDPOINT}/{entry['id']}", json=sheet_data, headers=self.auth_header)
