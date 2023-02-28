import pandas

# TODO Create small table how many different color squirrels there are and count them
# Output to a csv
# ,Fur Color,Count
# 0,grey,2473
# 1,red,392
# 2,black,103

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

color_counts = data["Primary Fur Color"].value_counts()
print(color_counts)

color_counts.to_csv("total_colors.csv")
