from bs4 import BeautifulSoup
import requests
import json
from poster import FormPoster

DATAFILE = input("Enter a file to dave the data as locally: (Ex: data.json): ")
URL = "https://www.zillow.com/homes/for_sale/"
params = {
    "searchQueryState": (
        '{"mapBounds":'
        '{"west":-120.807715421875,"east":-119.56626034375,'
        '"south":50.16275172026892,"north":51.173245251779626},'
        '"isMapVisible":true,'
        '"filterState":'
        '{"ah":{"value":true},"sort":{"value":"globalrelevanceex"}},'
        '"isListVisible":true}'
    )
}
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept": "*/*",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

# Get Location information and update the parameters:
print("Collecting Zone Information: ")
west_str = input("Enter West Coordinates: ")
east_str = input("Enter East Coordinates: ")
south_str = input("Enter South Coordinates: ")
north_str = input("Enter North Coordinates: ")

# Convert user inputs to floats
west = float(west_str)
east = float(east_str)
north = float(north_str)
south = float(south_str)

# Parse the JSON string and update the values
search_query_state = json.loads(params['searchQueryState'])
search_query_state['mapBounds']['west'] = west
search_query_state['mapBounds']['east'] = east
search_query_state['mapBounds']['north'] = north
search_query_state['mapBounds']['south'] = south

# Update the params dictionary with the updated searchQueryState
params['searchQueryState'] = json.dumps(search_query_state)

print(params)

# Initial URL Request
request = requests.get(url=f"{URL}", headers=HEADERS, params=params)
soup = BeautifulSoup(request.text, 'html.parser')

# Get total pages of results
total_pages = int(soup.find('span', {'class': 'Text-c11n-8-85-1__sc-aiai24-0 bEkett'}).text.split(" of ")[1])

for page in range(2, total_pages+1):
    request = requests.get(url=f"{URL}/{page}_p/", headers=HEADERS, params=params)

    # Get all json and transform into dict
    information = soup.find('script', {"data-zrr-shared-data-key": "mobileSearchPageStore"}).text.strip("<!--").strip("-->")
    information_dict = json.loads(information)
    house_result_dict = information_dict['cat1']['searchResults']['listResults']

    # Write information per page into data
    with open(file=DATAFILE, mode="a") as file:
        for listing in house_result_dict:
            house_info = {
                "url": f"{listing['detailUrl']}",
                "address": f"{listing['address']}",
                "space": f"{listing['area']}",
                "price": f"{listing['price']}"
            }
            json.dump(house_info, file)
            file.write('\n')


form_poster = FormPoster(DATAFILE)
