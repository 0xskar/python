import time
import requests
import math
from functions import is_close, sendmail, is_dark


# SMTP EMAIL STUFF currently configured to use smtp.sendgrid.net, 587. All other SMTP servers now
# cost money or want a phone number. This is the best free SMTP I could find besides setting one up.
YOUR_EMAIL = ""
YOUR_PASSWORD = ""
YOUR_COORDINATES = (50.7, -120.3)

running = True
while running:
    # GET ISS DATA
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    iss_coordinates = (float(latitude), float(longitude))

    # MATH for ISS Distance Calculation!
    lat1 = math.radians(YOUR_COORDINATES[0])
    lon1 = math.radians(YOUR_COORDINATES[1])
    lat2 = math.radians(iss_coordinates[0])
    lon2 = math.radians(iss_coordinates[1])
    distance = math.acos(math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2)*math.cos(lon2-lon1)) * 6371
    distance = distance * 1.609344
    distance = math.trunc(distance)

    if is_dark(latitude, longitude) and is_close(YOUR_COORDINATES, iss_coordinates):
        print("ISS IS CLOSE, and it should be dark, look up.")
        sendmail(distance, YOUR_EMAIL, YOUR_PASSWORD)
    else:
        print(f"ISS is far, currently {distance}KM away.")

    time.sleep(60)
