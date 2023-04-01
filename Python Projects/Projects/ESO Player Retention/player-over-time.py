import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file into a pandas DataFrame
df = pd.read_csv("steam_data.csv")

# Convert the "Month" column to datetime format
df["Month"] = pd.to_datetime(df["Month"], format="%B %Y")

# Plot a line chart of the average players over time
plt.plot(df["Month"], df["Average Players"])
plt.title("ESO Players over time")
plt.xlabel("Month")
plt.ylabel("Average Players")
plt.show()
