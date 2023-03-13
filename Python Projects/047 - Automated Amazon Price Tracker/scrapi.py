import os
from scraper import Scraper
import requests


class Scrapi:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {os.environ['STRAPI_API_KEY']}",
            "Content-Type": "application/json"
        }
        self.url_endpoint = "http://192.168.0.35:1337/api/amazon-price-trackers"
        self.scraper = Scraper()

    def post(self, data):
        item_name = data[1]
        item_url = data[0]
        item_price = data[2]
        wanted_price = int(input(f"Current price is {item_price}, enter a price to be notified at: "))
        params = {
            "data": {
                "name": item_name,
                "url": item_url,
                "wanted_price": wanted_price,
                "current_price": item_price
            }
        }
        r = requests.post(url=self.url_endpoint, headers=self.headers, json=params)
        print(f"Item Added:\n"
              f"Name:           {item_name}\n"
              f"Current Price:  {item_price}\n"
              f"Wanted Price:   {wanted_price}")

    def get(self):
        print("Getting all item in database...")
        r = requests.get(url=self.url_endpoint, headers=self.headers)
        tracked_items = r.json()['data']
        for item in tracked_items:
            print(f"Item ID:    {item['id']}\n"
                  f"Name:       {item['attributes']['name']}\n"
                  f"URL:        {item['attributes']['url']}\n"
                  f"Price:      {item['attributes']['current_price']}\n"
                  f"WTB Price:  {item['attributes']['wanted_price']}\n"
                  f"================================\n")

    def update(self):
        print("Updating Prices...")
        r = requests.get(url=self.url_endpoint, headers=self.headers)
        tracked_items = r.json()['data']
        for item in tracked_items:
            data = self.scraper.get_item(item['attributes']['url'])
            item_id = item['id']
            item_name = data[1]
            item_url = data[0]
            item_price = data[2]
            # insert price back into item current price
            params = {
                "data": {
                    "name": item_name,
                    "url": item_url,
                    "current_price": item_price
                }
            }
            r = requests.put(url=f"{self.url_endpoint}/{item_id}", headers=self.headers, json=params)
            print(f"Item No:{item_id} Updated:\n"
                  f"Name:           {item_name}\n"
                  f"Current Price:  {item_price}\n"
                  f"=========================\n")

    def price_scan(self):
        print("Performing Price Scan...\n"
              f"=======================================\n")
        r = requests.get(url=self.url_endpoint, headers=self.headers)
        tracked_items = r.json()['data']
        for item in tracked_items:
            target_price = float(item['attributes']['wanted_price'])
            current_price = float(item['attributes']['current_price'])
            item_name = item['attributes']['name']
            item_url = item['attributes']['url']
            if current_price < target_price:
                print(f"Sending email...\n"
                      f"{item_name} is lower then {target_price} @ {current_price}\n{item_url}\n"
                      f"=======================================\n")
