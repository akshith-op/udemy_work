from turtle import Turtle, Screen
import turtle as t
my_screen = Screen()
my_screen.bgcolor('black')
my_screen.title('Pong game')
my_screen.setup(width = 800, height = 600)
my_screen.tracer(0)
paddle_1 = Turtle()
paddle_2 = Turtle()
shape =((0, 0), (0 ,20), (-100,20 ), (-100, 0))
 
# registering the new shape
t.register_shape('paddle', shape)
 
# changing the shape to 'diamond'
paddle_1.shape('paddle')
paddle_1.color('white')
paddle_1.speed(10)
paddle_1.penup()
paddle_1.goto(x = 350, y = 0)
def move_up():
    new_y = paddle_1.ycor()+20
    paddle_1.goto(paddle_1.xcor(), new_y)
def move_down():
    new_y = paddle_1.ycor()-20
    paddle_1.goto(paddle_1.xcor(), new_y)

my_screen.listen()

my_screen.onkey(move_up,"w" )
my_screen.onkey(move_down, "s")


is_game_on = True
while is_game_on:
    my_screen.update()






my_screen.exitonclick()