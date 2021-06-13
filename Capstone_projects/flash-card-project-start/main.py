from tkinter import *
from numpy.core.records import record
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

# -----------------------------------------------------------------------------------------#

# -----------------------------------------------------------------------------------------#
data = pandas.read_csv("french_words.csv")


white_card = Canvas(width=800, height=526, highlightthickness=0, bg="#B1DDC6")
img_front = PhotoImage(file="card_front.png")
img123 = white_card.create_image(400, 263, image=img_front)
white_card.grid(column=0, row=0, columnspan=2)

data_file_list = data.to_dict(orient="records")
img_bak = PhotoImage(file="card_back.png")
r_french = {}


def random_word():
    global data
    global r_french, flip_timer
    window.after_cancel(flip_timer)
    r_french = random.choice(data_file_list)
    white_card.itemconfig(img123, image=img_front)
    word_french = r_french["French"]
    white_card.itemconfig(word_2, text=word_french, fill="black")
    white_card.itemconfig(word_1, text="French", fill="black")
    flip_timer = window.after(3000, enlish_card)


def enlish_card():
    white_card.itemconfig(img123, image=img_bak)
    word_english = r_french["English"]
    white_card.itemconfig(word_2, text=word_english, fill="white")
    white_card.itemconfig(word_1, text="English", fill="white")


def is_known():
    print(len(data_file_list))
    new_data = pandas.DataFrame(data_file_list)
    new_data.to_csv("words_to_learn")
    random_word()


wrg_image = PhotoImage(file="wrong.png")
wrong_bt = Button(
    image=wrg_image, highlightthickness=0, bg="#B1DDC6", command=random_word
)
wrong_bt.grid(column=0, row=1)


cr_image = PhotoImage(file="right.png")
right_bt = Button(image=cr_image, highlightthickness=0, bg="#B1DDC6", command=is_known)
right_bt.grid(column=1, row=1)

word_1 = white_card.create_text(400, 150, fill="black", font=("Arial", 40, "italic"))
word_2 = white_card.create_text(400, 263, fill="black", font=("Arial", 60, "bold"))
flip_timer = window.after(3000, enlish_card)
random_word()


# -----------------------------------------------------------------------------------------#


window.mainloop()
