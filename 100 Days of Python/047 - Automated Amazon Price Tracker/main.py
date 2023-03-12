from scraper import Scraper
from scrapi import Scrapi


running = True
while running:
    print("Main Menu:\n"
          "=========================\n"
          "1) Enter new item to track\n"
          "2) List all tracked items\n"
          "3) Update Current Prices\n"
          "4) Run Price Scan\n")

    prompt = input("Enter menu option: ")
    scraper = Scraper()
    scrapi = Scrapi()

    # Enter Amazon URL to Scrape Name, Price
    if prompt == "1":
        URL = input("Paste an Amazon URL to Track: ")
        scrapi.post(scraper.get_item(URL))

    if prompt == "2":
        scrapi.get()

    if prompt == "3":
        scrapi.update()

    if prompt == "4":
        scrapi.price_scan()
