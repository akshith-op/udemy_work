from turtle import Turtle, Screen
import time
import random

motion = True
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.tracer(0)
point = 0
snake_body = []
for i in range(3):
    snake = Turtle("square")
    snake.penup()
    snake.goto(x=point, y=0)
    point -= 20
    snake_body.append(snake)


def generate_food():
    global food
    food = Turtle()
    food.penup()
    rand_x = random.randint(-280, 280)
    rand_y = random.randint(-280, 280)
    # if snake_body[1:].xcor()-rand_x < and snake_body[1:].distance(food)
    food.goto(rand_x, rand_y)


generate_food()
while motion:
    time.sleep(0.1)
    my_screen.update()
    for idx in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[idx - 1].xcor()
        new_y = snake_body[idx - 1].ycor()
        snake_body[idx].goto(new_x, new_y)
    snake_body[0].fd(20)
    if snake_body[0].distance(food) < 20:
        generate_food()


my_screen.exitonclick()
