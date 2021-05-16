from turtle import Turtle, Screen
import turtle as t
import random
timmy = Turtle()
t.colormode(255)
def random_color():
    R = random.randint(1,255)
    G = random.randint(1,255)
    B = random.randint(1,255)
    color = (R,G,B)
    return(color)
def spirograph(size_of_gap):
    for i in range(360 // size_of_gap):
        timmy.color(random_color())
        timmy.speed('fastest')   
        timmy.circle(100)
        timmy.right(size_of_gap)
spirograph(1)


my_screen = Screen()
my_screen.exitonclick()