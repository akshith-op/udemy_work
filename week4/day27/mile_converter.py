from tkinter import *

window = Tk()
window.minsize(20, 20)
window.config(padx=50, pady=50)


def caluculate():
    miles = float(entry.get())
    km = miles * 1.609
    result.config(text=f"{km}")


mile_text = Label(text="Miles", font=("Arial", 15, "normal"))
mile_text.grid(column=3, row=1)

result_text = Label(text="is equals to", font=("Arial", 15, "normal"))
result_text.grid(column=1, row=2)

km = Label(text="Km", font=("Arial", 15, "normal"))
km.grid(column=3, row=2)

entry = Entry(width=5)
entry.focus()
entry.grid(column=2, row=1)

result = Label(text=0)
result.grid(column=2, row=2)

button = Button(text="Caluculate", command=caluculate)
button.grid(column=2, row=3)


window.mainloop()
