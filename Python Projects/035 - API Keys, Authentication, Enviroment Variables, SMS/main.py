import requests
from twilio.rest import Client

open_weather_API = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "79b94e44bff3061fe02cbe151cf0c8fc"
TWILIO_AUTH_TOKEN = ""
TWILIO_ACCOUNT_SID = ""

weather_params = {
    "id": 5989045,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(open_weather_API, params=weather_params)
weather_data = response.json()

weather_id = [weather['weather'][0]['id'] for weather in weather_data['list']]
weather_next_day = weather_id[0:4:]

# Check if it will rain/snow within the next 24 hours, then print if it will
will_rain = False
for _ in weather_next_day:
    print(_)
    if _ < 800:
        will_rain = True

if will_rain:
   # client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
   # message = client.messages.create(
   #     body="Errol Weather: It's probably going to rain/snow within the next 24 hours.",
   #     from_="+",
   #     to="+"
   # )
   # print(message.sid)
   print("It will probably rain next 24h")






