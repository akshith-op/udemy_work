from turtle import Turtle, Screen
import turtle as t
import time
import random

BG = "black"
motion = True
end = "GAME OVER"
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor(BG)
my_screen.title("Snake game")
my_screen.tracer(0)
score_turtle = Turtle()
score_turtle.color("white")
score_turtle.hideturtle()
end_turtle = Turtle()
end_turtle.color("white")
end_turtle.hideturtle()
snake_body = []


def set_snake():
    index = 0
    for i in range(3):
        snake = Turtle("square")
        snake.penup()
        snake.goto(x=index, y=0)
        index -= 20
        snake_body.append(snake)
    return index


index = set_snake()
new_index = index - 20


def increase_size_snake(index):
    snake = Turtle()
    snake.shape("square")
    snake.color(BG)
    snake.penup()
    snake_body.append(snake)
    index -= 20


def turn_right():
    snake_body[0].right(90)


def turn_left():
    snake_body[0].left(90)


food = Turtle()
food.speed("fastest")
food.shape("circle")
food.shapesize(0.8, 0.8)


def generate_food():
    rand_x = random.randint(-280, 280)
    rand_y = random.randint(-280, 280)
    food.penup()
    food.color("blue")
    food.goto(y=rand_y, x=rand_x)


generate_food()


def keys():
    my_screen.listen()
    if snake_body[0].heading() == 0:
        my_screen.onkey(key="Down", fun=turn_right)
        my_screen.onkey(key="Up", fun=turn_left)
    elif snake_body[0].heading() == 90:
        my_screen.onkey(key="Right", fun=turn_right)
        my_screen.onkey(key="Left", fun=turn_left)
    elif snake_body[0].heading() == 270:
        my_screen.onkey(key="Left", fun=turn_right)
        my_screen.onkey(key="Right", fun=turn_left)
    elif snake_body[0].heading() == 180:
        my_screen.onkey(key="Up", fun=turn_right)
        my_screen.onkey(key="Down", fun=turn_left)



def move():
    score = 0
    motion = True
    while motion:
        keys()
        my_screen.update()
        time.sleep(0.1)
        for idx in range(len(snake_body) - 1, 0, -1):
            if idx % 3 == 0:
                snake_body[idx].speed(0.5)
                snake_body[idx].color("green")
            elif idx % 3 == 1:
                snake_body[idx].color("white")
            else:
                snake_body[idx].color("orange")
            new_x = snake_body[idx - 1].xcor()
            new_y = snake_body[idx - 1].ycor()
            snake_body[idx].goto(new_x, new_y)
        snake_body[0].color("orange")
        snake_body[0].fd(20)
        for s in snake_body[1:]:
            if snake_body[0].distance(s) < 8:
                motion = False
                end_turtle.write(
                        f"{end}", align="center", font=("Arial", 24, "normal")
                    )

        if snake_body[0].distance(food) < 20:
            generate_food()
            score += 1
            score_turtle.penup()
            score_turtle.goto(0, 260)
            score_turtle.clear()
            score_turtle.write(
                f"Score: {score}", align="center", font=("Arial", 24, "normal")
            )
            increase_size_snake(new_index)

        if (
            snake_body[0].xcor() > 280 
            or snake_body[0].xcor() < -299
            or snake_body[0].ycor() > 299
            or snake_body[0].ycor() < -280
        ):
            end_turtle.write(f"{end}", align="center", font=("Arial", 24, "normal"))
            motion = False
        


move()
my_screen.exitonclick()
