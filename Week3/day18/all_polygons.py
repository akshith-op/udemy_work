from turtle import Turtle, Screen
import random


timmy_the_turtle = Turtle()
angles_dict = {
    'triangle': 3,
    'square': 4,
    'pentagon': 5,
    'hexagon': 6,
    'heptagon': 7,
    'octagon': 8,
    'nonagon': 9,
    'decagon': 10
} 
polygons = []
for i in angles_dict:
        polygons.append(i)
polygon = 0
def angles(angles_dict):
    for idx in range(len(polygons)):
        shape_polygon = polygons[idx+polygon]
        no_sides = angles_dict[shape_polygon]
        return no_sides
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", 'SeaGreen']
while True:
    color = random.choice(colours)
    timmy_the_turtle.color(color)
    no_sides = angles(angles_dict)
    angle = 360/no_sides    
    lines = 0
    while lines != no_sides:
        
        timmy_the_turtle.fd(100)
        lines+=1
        timmy_the_turtle.right(angle)
    polygon+=1
    if polygon == len(polygons):
        break
    else:
        angles(angles_dict)

my_screen = Screen()
my_screen.exitonclick()

