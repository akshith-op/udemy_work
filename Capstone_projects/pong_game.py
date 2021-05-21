from turtle import Turtle, Screen
import random
tim = Turtle()
my_screen = Screen()
def up():
    tim.setheading(90)
    tim.forward(100)

def down():
    tim.setheading(270)
    tim.forward(100)

def left():
    tim.set_heading(180)
    tim.forward(100)

def right():
    tim.setheading(0)
    tim.forward(100)
my_screen.listen()

my_screen.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
my_screen.onkey(down, "Down")
my_screen.onkey(left, "Left")
my_screen.onkey(right, "Right")

my_screen.mainloop()  # This will make sure the program continues to ru