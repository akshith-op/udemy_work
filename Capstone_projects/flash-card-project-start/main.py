from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

# -----------------------------------------------------------------------------------------#

white_card = Canvas(width=800, height=526, highlightthickness=0, bg="#B1DDC6")
img_front = PhotoImage(
    file="Users/Akshith/Github/udemy_work/Capstone_projects/flash-card-project-start/images/card_front.png"
)
white_card.create_image(400, 263, image=img_front)
white_card.grid(column=0, row=0, columnspan=2)

# -----------------------------------------------------------------------------------------#
data = pandas.read_csv(" ")
data_file = pandas.DataFrame(data)


def random_word():
    global data_file
    data_file_list = data_file.to_list()
    print(data_file_list)


wrg_image = PhotoImage(file="wrong.png")
wrong_bt = Button(image=wrg_image, highlightthickness=0, bg="#B1DDC6")
wrong_bt.grid(column=0, row=1)

cr_image = PhotoImage(file="right.png")
right_bt = Button(
    image=cr_image, highlightthickness=0, bg="#B1DDC6", command=random_word
)
right_bt.grid(column=1, row=1)

word_1 = white_card.create_text(
    400, 150, text="French", fill="black", font=("Arial", 40, "italic")
)
word_2 = white_card.create_text(
    400, 263, text="trouve", fill="black", font=("Arial", 60, "bold")
)

# -----------------------------------------------------------------------------------------#


window.mainloop()
