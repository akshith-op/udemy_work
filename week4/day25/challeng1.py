import pandas
data = pandas.read_csv("weather_data.csv")
maxi = data["temp"].max()
row = data[data.temp == maxi]
print(row)


monday = data[data.day == 'Monday']
c = monday.temp
f = (c * 9/5) + 32
print(f)