import datetime as dt
import smtplib
import email.message
import random

# email stuff for sendgrid smtp
YOUR_EMAIL = ""
YOUR_PASSWORD = ""

# get date with datetime monday == 1
now = dt.datetime.now()
day = now.weekday()


if day == 0:
    with open("quotes.txt", mode="r") as quotes:
        full_quotes = []
        for q in quotes:
            full_quotes.append(q)
        random_quote = random.choice(full_quotes)

    m = email.message.Message()
    m['From'] = "0xskar@proton.me"
    m['To'] = "eovogt@gmail.com"
    m['Subject'] = "Errol With Your motivational Monday!"
    m.set_payload(random_quote)

    connection = smtplib.SMTP("smtp.sendgrid.net", 587)
    connection.starttls()
    connection.login(user=YOUR_EMAIL, password=YOUR_PASSWORD)
    connection.sendmail(to_addrs=m['To'], from_addr=m['From'], msg=m.as_string())
    connection.close()
