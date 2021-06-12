
import pandas
def nat():
    text = str(input("please enter a word: "))
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    dict_data = {value.letter:value.code for (key,value) in data.iterrows()}
    try:
        nato = [dict_data[i.upper()] for i in text]
    except KeyError:
        print("Sorry, only letters in the the alphabet please.")
        nat()
    else:
        print(nato)
nat()





