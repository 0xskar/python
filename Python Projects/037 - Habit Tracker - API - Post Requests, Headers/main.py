import requests
import os
from datetime import datetime
import re

# see pixela graph here: https://pixe.la/v1/users/eovogt/graphs/graph1.html

# input number of minutes of yoga done today
minutes_done = 5

# Saved enviroment variable PIXELA_TOKEN
PIXELA_TOKEN = os.environ['PIXELA_TOKEN']
USERNAME = "eovogt"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# r = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(r.text)

# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_id = "graph1"

# graph_config = {
#     "id": graph_id,
#     "name": "Yoga Exercises",
#     "unit": "minutes",
#     "type": "int",
#     "color": "ajisai"
# }
#
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}
#
# r = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(r)

# Get today's date
today = datetime.today()
date_string = today.strftime('%Y%m%d')

new_graph_value = {
    "date": date_string,
    "quantity": str(minutes_done)
}

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}"

r = requests.post(url=graph_endpoint, json=new_graph_value, headers=headers)
print(r.text)
