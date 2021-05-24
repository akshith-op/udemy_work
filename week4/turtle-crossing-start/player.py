STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
# from turtle import Turtle, Screen
# import turtle as t
# import random
    self.my_screen = Screen()
my_screen.setup(700, 700)
tim = Turtle()
tim.shape('turtle')
tim.penup()
tim.left(90)
tim.goto(x = 0,y = -330)
my_screen.listen()
def move():
    tim.fd(30)
my_screen.onkey(move, key ='Up')
is_game_on = True
all_cars = []
while is_game_on:
    cars = Turtle()
    all_cars.append(cars)
    cars.penup()
    cars.setheading(180)

    cars.goto(330, random.randint(-330, 330))
    for i in all_cars:
        i.fd(30)
    















my_screen.exitonclick()
