from globals import *

spreadsheet_data = {
    "prices": [
        {
            "id": 0,
            "City": "Paris",
            "IATA Code": "",
            "Lowest Price": 54
        },
        {
            "id": 1,
            "City": "Berlin",
            "IATA Code": "",
            "Lowest Price": 42
        }
    ]
}


class DataManager:
    """This class is responsible for talking to the Google Sheet..Well it was until i realised Sheety was not a good
    deal at all..."""
    def __init__(self):
        self.auth_header = {
            "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
        }
        self.spreadsheet_data = spreadsheet_data

    def sheet_data_check(self):
        """Get all cities from flight_deals json with empty  IATA code"""
        # r = requests.get(url=SHEETY_API_ENDPOINT, headers=self.auth_header)
        # spreadsheet_data = r.json()
        data = [location for location in spreadsheet_data['prices']]
        return data

    def sheet_data_insert(self, data):
        """Insert data back into spreadsheet"""
        spreadsheet_data['prices'] = data
        print(spreadsheet_data)
