import csv
with open("weather_data.csv") as weather_data:
    data_file = csv.reader(weather_data)
    temperature = []
    for i in data_file:
        if i[1] != 'temp':
            temperature.append(i[1])
print(temperature)