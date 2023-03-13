import requests
from datetime import datetime
import os

# You have to setup a few of the environment variables to connect to APIs.
# Set for personalization:
GENDER = "male"
WEIGHT_KG = 99.79
HEIGHT_CM = 190.52
AGE = 36

# NUTRITIONIX ENDPOINT - Estimate calories burned for exercises using natural language:
#  POST https://trackapi.nutritionix.com/v2/natural/exercise
NUTRITIONIX_URL_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_APP_ID = os.environ["NUTRITIONIX_APP_ID"]
NUTRITIONIX_API_KEY = os.environ["NUTRITIONIX_API_KEY"]

# SHEETY.CO ENDPOINT
SHEETY_BEARER_TOKEN = os.environ["SHEETY_BEARER_TOKEN"]
SHEETY_USERNAME = "720b14bb86924f26582e95ebbab971fa"
SHEETY_PROJECT_NAME = "myWorkouts"
SHEETY_SHEET_NAME = "workouts"
SHEETY_URL_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}"

# Code
exercise = input("What exercise did you do today? ")

nutritionx_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "Content-Type": "application/json"
}

post_request = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# get nutritionix calorie information from input
r = requests.post(url=NUTRITIONIX_URL_ENDPOINT, headers=nutritionx_headers, json=post_request)
nutritionix_result = r.json()
print(nutritionix_result)

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

# Getting Rows - return all records in out sheet
r = requests.get(url=SHEETY_URL_ENDPOINT, headers=sheety_headers)
sheet_result = r.json()

# Getting information we need from sheet_result for Sheety
date = datetime.today()
date = date.strftime('%d/%m/%Y')
time = datetime.now()
time = time.strftime('%H:%M:%S')
type_of_exercise = nutritionix_result['exercises'][0]['user_input']
length_of_exercise = nutritionix_result['exercises'][0]['duration_min']
calories = nutritionix_result['exercises'][0]['nf_calories']

print()

# Adding a new row with the nutiotionix json output
sheety_input = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": type_of_exercise,
        "duration": length_of_exercise,
        "calories": calories
    }
}

r = requests.post(url=SHEETY_URL_ENDPOINT, json=sheety_input, headers=sheety_headers)
