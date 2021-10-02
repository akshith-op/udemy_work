from turtle import Turtle, Screen
import turtle as t
import time
import random

# Define constants
BG = "black"
startText = 'Press "space" button to start the game'
end = "GAME OVER"
motion = False

# Define global objects
my_screen = Screen()
score_turtle = Turtle()
end_turtle = Turtle()
food = Turtle()
snake_body = []
tail_index = 0

# Init global objects
def init():
    my_screen.setup(width=600, height=600)
    my_screen.bgcolor(BG)
    my_screen.title("Snake game")
    my_screen.tracer(0)

    score_turtle.color("white")
    score_turtle.hideturtle()

    end_turtle.color("white")
    end_turtle.hideturtle()

    tail_index = 0


# Set initial position of snake
def init_snake_position():
    index = 0
    for i in range(3):
        snake = Turtle("square")
        snake.penup()
        snake.goto(x=index, y=0)
        index -= 20
        snake_body.append(snake)

    tail_index = index - 20
    return index


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


def start_game():
    global motion
    motion = True


def ignore_key_press():
    pass


def init_food():
    food.speed("fastest")
    food.shape("circle")
    food.shapesize(0.8, 0.8)


def generate_food():
    rand_x = random.randint(-280, 280)
    rand_y = random.randint(-280, 280)
    food.penup()
    food.color("blue")
    food.goto(y=rand_y, x=rand_x)


def on_key_press():
    my_screen.listen()
    # snaking moving in right direction
    if snake_body[0].heading() == 0:
        my_screen.onkey(key="Down", fun=turn_right)
        my_screen.onkey(key="Up", fun=turn_left)
        my_screen.onkey(key="Right", fun=ignore_key_press)
        my_screen.onkey(key="Left", fun=ignore_key_press)
    elif snake_body[0].heading() == 90:
        my_screen.onkey(key="Right", fun=turn_right)
        my_screen.onkey(key="Left", fun=turn_left)
        my_screen.onkey(key="Up", fun=ignore_key_press)
        my_screen.onkey(key="Down", fun=ignore_key_press)
    elif snake_body[0].heading() == 270:
        my_screen.onkey(key="Left", fun=turn_right)
        my_screen.onkey(key="Right", fun=turn_left)
        my_screen.onkey(key="Up", fun=ignore_key_press)
        my_screen.onkey(key="Down", fun=ignore_key_press)
    elif snake_body[0].heading() == 180:
        my_screen.onkey(key="Up", fun=turn_right)
        my_screen.onkey(key="Down", fun=turn_left)
        my_screen.onkey(key="Right", fun=ignore_key_press)
        my_screen.onkey(key="Left", fun=ignore_key_press)


def start_play():
    global motion
    motion = False
    end_turtle.penup()
    end_turtle.goto(y=100, x=0)
    end_turtle.write(f"{startText}", align="center", font=("Arial", 24, "normal"))
    while True:
        my_screen.listen()
        my_screen.onkey(key="space", fun=start_game)
        if motion == True:
            break
        time.sleep(0.1)
        my_screen.update()
    end_turtle.clear()
    generate_food()


def play():
    global motion
    score = 0
    start_play()

    while motion:
        on_key_press()
        my_screen.update()
        time.sleep(0.1)
        for idx in range(len(snake_body) - 1, 0, -1):
            if idx % 2 == 0:
                snake_body[idx].speed(0.5)
                snake_body[idx].color("cyan")
            elif idx % 2 == 1:
                snake_body[idx].color("white")
            new_x = snake_body[idx - 1].xcor()
            new_y = snake_body[idx - 1].ycor()
            snake_body[idx].goto(new_x, new_y)
        snake_body[0].color("red")
        snake_body[0].shape("circle")
        snake_body[0].fd(20)

        for s in snake_body[1:]:
            if snake_body[0].distance(s) < 8:
                motion = False
                end_turtle.goto(0, 0)
                end_turtle.write(f"{end}", align="center", font=("Arial", 24, "normal"))

        if snake_body[0].distance(food) < 20:
            generate_food()
            score += 1
            score_turtle.penup()
            score_turtle.goto(0, 260)
            score_turtle.clear()
            score_turtle.write(
                f"Score: {score}", align="center", font=("Arial", 24, "normal")
            )
            increase_size_snake(tail_index)

        if snake_body[0].ycor() > 299 or snake_body[0].ycor() < -280:
            end_turtle.write(f"{end}", align="center", font=("Arial", 24, "normal"))
            motion = False
        elif snake_body[0].xcor() > 280 or snake_body[0].xcor() < -299:
            portal = snake_body[0].xcor() * -1
            y = snake_body[0].ycor()
            snake_body[0].goto(portal, y)


init()
init_snake_position()
init_food()
play()
my_screen.exitonclick()
