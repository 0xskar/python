import os

# YOUR LOCAL AIRPORT OR WHERE FLYING FROM
LOCAL_IATACODE = "YKA"

# REQUIRED APIs
STRAPI_API_KEY = os.environ["STRAPI_API_KEY"]
STRAPI_URL_ENDPOINT = f"http://192.168.0.35:1337/api/flight-datas"
STRAPI_HEADERS = {
    "Authorization": f"Bearer {STRAPI_API_KEY}",
    "Content-Type": "application/json"
}

TEQUILA_FLIGHT_SEARCH_API_KEY = os.environ["TEQUILA_FLIGHT_SEARCH_API_KEY"]
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_HEADERS = {
    "Content-Type": "application/json",
    "apikey": TEQUILA_FLIGHT_SEARCH_API_KEY
}
