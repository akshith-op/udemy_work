import pandas

data_dict = {"students": ["akshith", "ashwath", "shivani"], "score": [90, 88, 75]}

frame = pandas.DataFrame(data_dict)
print(frame)
frame.to_csv("new_data.csv")