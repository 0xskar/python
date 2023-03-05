import smtplib
import email.message
import requests
from datetime import datetime


def is_close(your_coordinates, iss_coordinates):
    # Define acceptable range
    higher_x, lower_x = your_coordinates[0] + 5, your_coordinates[0] - 5
    x_range = (lower_x, higher_x)
    higher_y, lower_y = your_coordinates[1] + 5, your_coordinates[1] - 5
    y_range = (lower_y, higher_y)
    if x_range[0] < iss_coordinates[0] < x_range[1] and y_range[0] < iss_coordinates[1] < y_range[1]:
        return True
    else:
        return False


def sendmail(distance, send_to_email, password):
    m = email.message.Message()
    m['From'] = send_to_email
    m['To'] = send_to_email
    m['Subject'] = f"ISS is close! It's {distance}KM away!"
    m.set_payload("The ISS is probably passing overhead right now, check it out!\nFrom Errol")

    connection = smtplib.SMTP("smtp.sendgrid.net", 587)
    connection.starttls()
    connection.login(user=send_to_email, password=password)
    connection.sendmail(to_addrs=m['To'], from_addr=m['From'], msg=m.as_string())
    connection.close()


def is_dark(latitude, longitude):
    # PARAMETERS to pass to find out when the sun is down
    parameters = {
        "lat": latitude,
        "lng": longitude,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False

