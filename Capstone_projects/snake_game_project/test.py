from turtle import Turtle, Screen
import turtle as t
import time
import random

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor('cyan')
my_screen.tracer(0)

snake_body = []
index = 0
for i in range(3):
    snake = Turtle('square')
    
    snake.penup()
    snake.goto(x = index, y = 0)
    index-=20
    snake_body.append(snake)
# def increase_size_snake(index):
#     snake = Turtle(index)
#     snake.goto(x = index, y = 0)
#     index-=20
# snake.increase_size_snake(index)
def turn_right():
    snake_body[0].right(90)
    move()
def turn_left():
    snake_body[0].left(90)
food = Turtle()
food.speed('fastest')
food.shape('circle')
food.shapesize(0.5,0.5)
rand_x = random.randint(-580,580)
rand_y = random.randint(-580, 580)
food.goto(y = rand_y, x = rand_x)

def move(): 
    motion = True
    while motion:
        my_screen.update()
        time.sleep(0.1)
        for idx in range(len(snake_body) - 1, 0, -1):
            snake_body[idx].speed(0.5)
            new_x = snake_body[idx - 1].xcor()
            new_y = snake_body[idx - 1].ycor()
            snake_body[idx].goto(new_x, new_y)
        snake_body[0].fd(20)
        my_screen.listen()
        if snake_body[0].heading() == 0:
            my_screen.onkey(key = 's',fun = turn_right)
            my_screen.onkey(key = 'w',fun = turn_left)
        elif snake_body[0].heading() == 90:
            my_screen.onkey(key = 'd',fun = turn_right)
            my_screen.onkey(key = 'a',fun = turn_left)
        elif snake_body[0].heading() == 270:
            my_screen.onkey(key = 'a',fun = turn_right)
            my_screen.onkey(key = 'd',fun = turn_left)
        else:
            my_screen.onkey(key = 'w',fun = turn_right)
            my_screen.onkey(key = 's',fun = turn_left)
            
        

move()

    















my_screen.exitonclick()