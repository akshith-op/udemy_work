from tkinter import *
import math
from playsound import playsound


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 4
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
MARKS = "✔"
_marks = "✔ ✔ ✔ ✔"
reps = 0
time = None
check_marks = None
mark5 = "    "


def time_reset():
    global check_marks
    global MARKS
    global reps
    MARKS = " "
    check_marks.config(text=MARKS, bg="#0cb1f8")
    time.config(text="Start", command=start_play)
    reset.config(text="Reset", command=time_reset)
    time.grid(column=0, row=2)
    reset.grid(column=2, row=2)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    text.config(text="Timer")
def play_time():
    window.after(1,start_play)

def pause_time():
    window.after_cancel(timer)
    time.config(text="Play ", command=play_time)


def start_play():
    time.config(text="Pause", command=pause_time)
    global _marks
    global reps
    global MARKS
    global check_marks
    reps += 1
    work_time = WORK_MIN * 1
    break_ = SHORT_BREAK_MIN * 1
    long_break = LONG_BREAK_MIN * 1
    if reps <= 8:
        if reps % 8 == 0:
            text.config(text="break", fg="#01fe07")
            check_marks.config(text=_marks, bg="#0cb1f8")
            # playsound("20_min_break_done.mp3")
            count_down(long_break)
        elif reps % 2 == 0:
            # playsound("25_min.mp3")
            text.config(text="break", fg="#ffe013")
            check_marks = Label(text=MARKS, bg="#0cb1f8")
            MARKS += " ✔"
            check_marks.grid(column=1, row=3)
            count_down(break_)
        else:
            count_down(work_time)
            text.config(text="Work", fg="#800080")
            # if reps != 1:
            # playsound("5_min_done.mp3")
            # playsound("tenet.mp3")
    else:
        text.config(text="Done....", fg="#00FF00")
        time.grid_forget()
        reset.grid(column=1, row=4)
        # playsound("20min_done.mp3")


def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    if sec == 0:
        sec = "00"
    elif sec < 10:
        sec = f"0{sec}"
    elif min < 10:
        min = f"0{min}"
    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{min}:{sec}")
        global timer
        global reps
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps <= 8:
            start_play()


window = Tk()
window.title("Pomodoro")
window.config(padx=30, pady=30, bg="#0cb1f8")

text = Label(text="Timer", fg="black", font=(FONT_NAME, 50, "normal"), bg="#0cb1f8")
text.grid(column=1, row=0)

reset = Button(text="Reset", highlightthickness=0, command=time_reset, bg="blue")
reset.grid(column=2, row=2)

time = Button(text="Start", highlightthickness=0, command=start_play, bg="blue")
time.grid(column=0, row=2)


canvas = Canvas(width=200, height=224, bg="#0cb1f8", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=("FONT_NAME", 35, "bold")
)
canvas.grid(column=1, row=1)


window.mainloop()
