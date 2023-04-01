import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the webpage
url = "https://steamcharts.com/app/306130"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table that contains the data we need
table = soup.find("table", {"class": "common-table"})

# Find the rows in the table
rows = table.find_all("tr")

# Write the data to a CSV file
with open("steam_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Month", "Average Players"])  # write the header row
    for row in rows[1:]:  # skip the header row
        columns = row.find_all("td")
        month = columns[0].get_text().strip()
        avg_players = columns[1].get_text().strip()
        writer.writerow([month, avg_players])
