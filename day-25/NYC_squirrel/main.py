import pandas as pd

squirrel_data = pd.read_csv("squirrel_count.csv")


gray_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
red_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
black_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]

gray_count = gray_color["Primary Fur Color"].count()
red_count = red_color["Primary Fur Color"].count()
black_count = black_color["Primary Fur Color"].count()


squirrel_count = {
    "Fur Color": ["Gray", "Black", "Red"],
    "Count": [gray_count, black_count, red_count]
}

data = pd.DataFrame(squirrel_count)
data.to_csv("s_count.csv")