import turtle as t
from turtle import Turtle, Screen
import random
timmy_the_turtle = t.Turtle()
t.colormode(255)
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", 'SeaGreen']
# color = random.choice(colours)
directions = [0,90,180,270]
timmy_the_turtle.speed(100)
timmy_the_turtle.pensize(15)
def random_color():
    R = random.randint(1,255)
    G = random.randint(1,255)
    B = random.randint(1,255)
    color = (R,G,B)
    return(color)


loop = 0
while loop != 200 :
    
    movement = random.choice(directions)
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.setheading(movement)
    timmy_the_turtle.fd(30)
    loop+=1




my_screen = Screen()
my_screen.exitonclick()