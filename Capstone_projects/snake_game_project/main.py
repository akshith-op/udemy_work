import turtle as t
from turtle import Turtle, Screen
POS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANE = 20

class Snake:

    def __init__(self):
        self.snake_body = []
        self.increase__size_snake()

    def increase__size_snake(self):
        for i in POS:
            snake = Turtle('square')
            snake.penup()
            snake.goto(i)      
            self.snake_body.append(snake)

    def move(self):
        for idx in range(len(self.snake_body)-1, 0 , -1):
            new_x = self.snake_body[idx-1].xcor()
            new_y = self.snake_body[idx-1].ycor()
            self.snake_body[idx].goto(new_x, new_y)
        self.snake_body[0].fd(MOVE_DISTANE)

from turtle import Turtle,Screen
import time


my_screen = Screen()
my_screen.setup(height = 700, width = 800)
my_screen.bgcolor('cyan')
my_screen.title('Snake game')
my_screen.tracer(0)

game = Snake()

motion = True
while motion:
    my_screen.update()
    time.sleep(0.1)
    game.move()
    motion = False












my_screen.exitonclick()