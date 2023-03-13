# import smtplib
#
# connection = smtplib.SMTP("smtp.sendgrid.net", 587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday()

date_of_birth = dt.datetime(year=1986, month=8, day=3)
print(date_of_birth.weekday())
