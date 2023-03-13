from bs4 import BeautifulSoup
import requests
import re


class Scraper:
    def __init__(self):
        self.item_url = None
        self.item_name = None
        self.item_price = None
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
            "Accept-Language": "en-US,en;q=0.5"
        }

    def get_item(self, item_url):
        self.item_url = item_url
        r = requests.get(url=self.item_url, headers=self.headers)
        html = BeautifulSoup(r.text, 'html.parser')

        # Get Product Name
        self.item_name = html.find(id="productTitle").get_text().lstrip()

        # Get Product Price
        try:
            self.item_price = html.find(id="corePrice_feature_div").find("span", {"class": "a-offscreen"}).text.strip("$")
        except AttributeError:
            self.item_price = html.find(id="price").text.strip("$")
        return [self.item_url, self.item_name, self.item_price]
