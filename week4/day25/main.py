import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(type(data))
print(data['temp'])
print(type(data['temp']))
data_dict = data.to_dict()
print(data_dict, 1)
temp_list = data["temp"].to_list()
# av = sum(temp_list) / len(temp_list)
# print(round(av))
series = data['temp']
print(round(series.mean()))
print(f"the highest temp: {series.max()}")
print(f"{data[data.day == 'Monday']} the row")
 