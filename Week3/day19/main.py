from turtle import Turtle,Screen 
import turtle as t
tim = Turtle()
my_screen = Screen()
def function():
    tim.fd(50)
def turn_right():
    tim.right(90)
my_screen.listen()
my_screen.onkey(key = "space", fun = function)
# my_screen.onkey('key = w', fun = turn_right)



my_screen.exitonclick()