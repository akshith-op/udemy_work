
import pandas
def Nato(text):
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    dict_data = {value.letter:value.code for (key,value) in data.iterrows()}
    nato = [dict_data[i.upper()] for i in text]
    return nato
result = Nato(str(input("please enter a word: ")))
print(result)

