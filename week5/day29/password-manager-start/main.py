from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_entry.delete(0, END)
    import random

    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password = []
    password_l = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_n = [random.choice(symbols) for sign in range(random.randint(2, 4))]
    password_s = [random.choice(numbers) for sign in range(random.randint(2, 4))]
    password = password_l + password_s + password_n
    random.shuffle(password)
    the_password = "".join(password)
    password_entry.insert(0, the_password)
    pyperclip.copy(password_entry.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    if len(website.get()) > 0 and len(password_entry.get()) > 0:
        is_ok = messagebox.askokcancel(
            title=website.get(),
            message=f"These are the details entered: \nEmail: {email.get()}\nPassword: {password_entry.get()}\nIs it ok to save?",
        )
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(
                    f"{website.get()} | {email.get()} | {password_entry.get()}\n"
                )
                website.delete(0, END)
                password_entry.delete(0, END)
                website.focus()
    else:
        messagebox.showinfo(title="Oops!", message="Please don't any field empty!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg="#5856d6")
window.title("Password manager")

canvas = Canvas(width=200, height=200, bg="#5856d6", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_txt = Label(text="Website: ", bg="#5856d6", font=("Arial", 15))
website_txt.grid(column=0, row=1)
website = Entry(width=35, highlightthickness=0)
website.focus()
website.grid(column=1, row=1, columnspan=2)

# ---------------------------------------------------------------------- #

email_txt = Label(text="Email: ", bg="#5856d6", font=("Arial", 15))
email_txt.grid(column=0, row=2)
email = Entry(width=35, highlightthickness=0)
email.insert(END, "akshith.isola@gmail.com")
email.grid(column=1, row=2, columnspan=2)

# ---------------------------------------------------------------------- #

passwod_txt = Label(text="Password: ", bg="#5856d6", font=("Arial", 15))
passwod_txt.grid(column=0, row=3)
password_entry = Entry(width=21, highlightthickness=0)
password_entry.grid(column=1, row=3)

# ---------------------------------------------------------------------- #

generate = Button(
    text="Generate Password", command=password_generator, highlightthickness=0, width=14
)
generate.grid(column=2, row=3)

# ---------------------------------------------------------------------- #

add = Button(text="Add", command=add_data, highlightthickness=0, width=36)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()
