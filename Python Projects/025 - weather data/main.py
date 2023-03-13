# with open("weather-data.csv") as data_file:
#     data = data_file.readlines()
#
# print(data)

# import csv
#
# current_data = []
#
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

data = pandas.read_csv("weather-data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# temperature_list = data["temp"].to_list()
# print(temperature_list)
#
# average_temperatue = sum(temperature_list) / len(temperature_list)
# print(average_temperatue)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data.temp)
#
# print(data[data["day"] == "Monday"])
#
# #max
# print(data[data.temp == data.temp.max()])
#
# # get a cell inside a dataframe
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

#dataframe from scratch
data_dict = {
    "students": ["Oskar", "James", "Othello"],
    "scores": [99, 12, 45]
}
data = pandas.DataFrame(data_dict)
print(data)

#convert data to csv

data.to_csv("new_data.csv")

