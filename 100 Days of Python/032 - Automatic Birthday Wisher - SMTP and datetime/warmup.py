# import smtplib
#
# my_email = "apikey"
# password = "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"
#
# connection = smtplib.SMTP("smtp.sendgrid.net", 587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="eovogt@gmail.com", msg="From: 0xskar@proton.me\nSubject: [PGS]: Results\n\nBlaBlaBla")
# connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday()

date_of_birth = dt.datetime(year=1986, month=8, day=3)
print(date_of_birth.weekday())
