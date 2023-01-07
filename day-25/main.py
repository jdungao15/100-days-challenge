# with open("weather_data.csv") as data_contents:
#     data = data_contents.readlines()
# print(data)

# import csv
# with open("weather_data.csv") as data_contents:
#     data = csv.reader(data_contents)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")

data_dict = data.to_dict()
temp_list = data["temp"].to_list()
max_temp = data["temp"].max()

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = (monday.temp * 1.8) + 32
print(monday_temp)