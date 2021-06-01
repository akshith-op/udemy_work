from tkinter import *

window = Tk()
window.title("distance")
window.minsize(555, 555)
window.config(padx = 200, pady= 200)


def button1():
    print("i got clicked")
    my_label.config(text=input.get().title())


my_label = Label(text="my name is akshith", font=("Arial", 24, "italic"))
my_label.config(text="i am sleeping")
my_label.grid(column=0, row = 0)

button = Button(text="click me", command=button1)
button.grid(column=1, row = 1)

input = Entry(width=10)
input.grid(column=2, row = 2)


window.mainloop()
