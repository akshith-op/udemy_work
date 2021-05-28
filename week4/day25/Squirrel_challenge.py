import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Graycolor = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamoncolor = len(data[data["Primary Fur Color"] == "Cinnamon"])
Blackcolor = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "count": [Graycolor, Cinnamoncolor, Blackcolor],
    "fur color": ["Gray", "Cinnamon", "Black"],
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
