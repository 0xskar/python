import requests


open_weather_API = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "79b94e44bff3061fe02cbe151cf0c8fc"

weather_params = {
    "id": 5989045,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(open_weather_API, params=weather_params)
weather_data = response.json()
print(weather_data)

