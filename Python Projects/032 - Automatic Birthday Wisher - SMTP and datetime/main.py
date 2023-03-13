import smtplib
import email.message
import datetime as dt
import os
import random
import pandas as pd

# email stuff for sendgrid smtp
YOUR_EMAIL = ""
YOUR_PASSWORD = ""


date = dt.date
today_day = date.today().day
today_month = date.today().month
today = (today_month, today_day)

print(f"Today: {today}")

birthday_data = pd.read_csv("birthdays.csv")

birthdays_dict = {(row['month'], row['day']): row['name'] for (index, row) in birthday_data.iterrows()}

if today in birthdays_dict:
    # get whomever birthday name
    birthday_name = birthdays_dict[today]
    # get a random letter from templates
    template_directory = "./letter_templates"
    letters = os.listdir(template_directory)
    random_letter = random.choice(letters)
    # open and replace the [NAME] within the letter
    with open(os.path.join(template_directory, random_letter), 'r') as f:
        custom_letter = f.read()
        custom_letter = custom_letter.replace("[NAME]", birthday_name)

    m = email.message.Message()
    m['From'] = "0xskar@proton.me"
    m['To'] = "eovogt@gmail.com"
    m['Subject'] = f"It is {birthday_name}'s birthday!"
    m.set_payload(custom_letter)

    connection = smtplib.SMTP("smtp.sendgrid.net", 587)
    connection.starttls()
    connection.login(user=YOUR_EMAIL, password=YOUR_PASSWORD)
    connection.sendmail(to_addrs=m['To'], from_addr=m['From'], msg=m.as_string())
    connection.close()