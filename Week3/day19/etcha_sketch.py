from turtle import Turtle, Screen
import turtle as t
my_screen = Screen()


timmy_the_turtle = Turtle()

def move_forward():
    timmy_the_turtle.fd(10)

def move_backward():
    timmy_the_turtle.bk(10)

def turn_left():
    new = timmy_the_turtle.heading()+10
    timmy_the_turtle.setheading(new)

def turn_right():
    new = timmy_the_turtle.heading()-10
    timmy_the_turtle.setheading(new)

def clear():
    timmy_the_turtle.clear()
    timmy_the_turtle.penup()
    timmy_the_turtle.home()
    timmy_the_turtle.pendown()

my_screen.listen()
my_screen.onkey(key = 'w',fun = move_forward)
my_screen.onkey(key = 's',fun = move_backward)
my_screen.onkey(key = 'd',fun = turn_left)
my_screen.onkey(key = 'a',fun = turn_right)
my_screen.onkey(key = 'c',fun = clear)












my_screen.exitonclick()