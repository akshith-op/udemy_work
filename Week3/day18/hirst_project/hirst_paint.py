# import colorgram
import random
import turtle as t
from turtle import Turtle, Screen
t.colormode(255)


# extracted_colors = []
# colors = colorgram.extract("Week3/day18/hirst_project/image.jpg", 30)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     extracted_colors.append(new_color)
# print(extracted_colors)

color_list = [
    (254, 253, 250),
    (235, 246, 250),
    (251, 241, 246),
    (245, 252, 249),
    (243, 235, 74),
    (211, 158, 93),
    (186, 12, 69),
    (112, 179, 208),
    (25, 116, 168),
    (173, 171, 31),
    (219, 129, 166),
    (161, 79, 35),
    (129, 185, 146),
    (9, 32, 76),
    (222, 62, 105),
    (235, 73, 42),
    (180, 45, 94),
    (30, 136, 81),
    (236, 164, 193),
    (78, 12, 63),
    (12, 54, 33),
    (234, 227, 7),
    (26, 165, 209),
    (16, 43, 132),
    (58, 166, 96),
    (134, 214, 229),
    (10, 101, 63),
    (133, 34, 20),
    (91, 27, 11),
    (159, 211, 188),

]
timmy_the_turtle = Turtle()
timmy_the_turtle.speed('fastest')
timmy_the_turtle.penup()
timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)
def painting(dot_count):
    for i in range(1,dot_count+1 ):
        color = random.choice(color_list)
        timmy_the_turtle.penup()
        timmy_the_turtle.fd(50)
        timmy_the_turtle.dot(20,color)
dot_count = int(input("pls enter the count of dots: "))
painting(dot_count)
row = 1
while row != dot_count:
    timmy_the_turtle.penup()
    timmy_the_turtle.left(90)
    timmy_the_turtle.fd(50)
    timmy_the_turtle.left(90)
    timmy_the_turtle.fd(dot_count*50)
    timmy_the_turtle.left(180)
    row+=1
    painting(dot_count)







my_screen = Screen()
my_screen.exitonclick()



