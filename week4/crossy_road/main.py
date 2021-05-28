from turtle import Turtle, Screen
import turtle as t
import random
import time
import pandas
speed = 10
my_screen = Screen()
my_screen.tracer(0)
my_screen.setup(700, 700)
tim = Turtle()
tim.shape("turtle")
tim.penup()
tim.left(90)
tim.goto(x=0, y=-330)
my_screen.listen()


def move_fd():
    tim.fd(30)


def move_bk():
    if tim.ycor() > -330:
        tim.bk(30)
    else:
        pass


my_screen.onkey(move_fd, key="Up")
my_screen.onkey(move_bk, key="Down")

is_game_on = True
t.colormode(255)


def random_color():
    R = random.randint(1, 255)
    G = random.randint(1, 255)
    B = random.randint(1, 255)
    color = (R, G, B)
    return color


time.sleep(0.1)
all_cars = []


def car_movement():
    time.sleep(0.1)
    my_screen.update()
    random_chance = random.randint(1, 3)
    if random_chance == 1:
        cars = Turtle()
        cars.shape("square")
        cars.shapesize(1, 2)
        cars.color(random_color())
        cars.penup()
        cars.setheading(180)
        cars.goto(300, random.randint(-300, 300))
        all_cars.append(cars)
    else:
        pass


def reset():
    tim.goto(x=0, y=-330)


level = 1
ON_turtle = Turtle()
ON_turtle.penup()
ON_turtle.hideturtle()
ON_turtle.goto(x=-200, y=310)

ON_turtle.write(f"Level: {level}", align="center", font=("Arial", 24, "normal"))
while is_game_on:

    car_movement()
    for i in all_cars:
        i.fd(speed)
        if tim.distance(i) < 23:
            is_game_on = False
            ON_turtle = Turtle()
            ON_turtle.hideturtle()
            on = "GAME OVER"
            ON_turtle.write(f"{on}", align="center", font=("Arial", 24, "normal"))
        elif tim.ycor() > 330:
            level += 1
            ON_turtle.clear()
            ON_turtle.write(
                f"Level: {level}", align="center", font=("Arial", 24, "normal")
            )
            speed += 2
            reset()


my_screen.exitonclick()
