from bs4 import BeautifulSoup
import requests
import json

URL = "https://www.zillow.com/homes/for_sale/"
QUERY = "?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-120.807715421875%2C%22east%22%3A-119.56626034375%2C%22south%22%3A50.16275172026892%2C%22north%22%3A51.173245251779626%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept": "*/*",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

# Initial URL Request
request = requests.get(url=f"{URL}{QUERY}", headers=HEADERS)
soup = BeautifulSoup(request.text, 'html.parser')

# Get total pages of results
total_pages = int(soup.find('span', {'class': 'Text-c11n-8-85-1__sc-aiai24-0 bEkett'}).text.split(" of ")[2])

# TODO for page in total_pages request and append to complete_results
complete_results = []

for page in range(2, total_pages+1):
    request = requests.get(url=f"{URL}/{page}_p/{QUERY}", headers=HEADERS)

    # Get all json and transform into dict
    information = soup.find('script', {"data-zrr-shared-data-key": "mobileSearchPageStore"}).text.strip("<!--").strip("-->")
    information_dict = json.loads(information)
    house_result_dict = information_dict['cat1']['searchResults']['listResults']

    # Write information per page into data
    with open(file="data.json", mode="a") as file:
        for listing in house_result_dict:
            house_info = {
                "url": f"{listing['detailUrl']}",
                "address": f"{listing['address']}",
                "space": f"{listing['area']}",
                "price": f"{listing['price']}"
            }
            json.dump(house_info, file)
            file.write('\n')


