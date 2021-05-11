from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')

timmy_the_turtle.color("coral")
timmy_the_turtle.pencolor('blue')
right = 0
for i in range(4):
    timmy_the_turtle.speed(1)
    timmy_the_turtle.fd(100)
    if right >=3:
        break
    timmy_the_turtle.right(90)
    right+=1
    if right > 3:
        break




























my_screen = Screen()
my_screen.exitonclick()