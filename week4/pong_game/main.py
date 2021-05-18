from turtle import Turtle, Screen
import turtle as t
from paddle import Paddle
my_screen = Screen()
my_screen.bgcolor('black')
my_screen.title('Pong game')
my_screen.setup(width = 800, height = 600)
my_screen.tracer(0)
r_paddle = Paddle(350)
l_paddle = Paddle(-350)


# def move_up(self)
#         new_y = self.ycor()+20
#         self.goto(xcor, new_y)
#     def move_down():
#         new_y = self.ycor()-20
#         self.goto(xcor, new_y)
#     # my_screen.listen()

#     # my_screen.onkey(move_up,"w" )
#     # my_screen.onkey(move_down, "s")
            
my_screen.exitonclick()
is_game_on = True
while is_game_on:
    my_screen.update()






