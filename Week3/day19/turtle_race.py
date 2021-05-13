from turtle import Turtle, Screen
import turtle as t
import colorgram
import random
t.colormode(255)

# colors_list = []
# colors = colorgram.extract("image2.jpg", 7)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new = (r, g, b)
#     colors_list.append(new)
colors_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo' ,'violet']
is_race_on = False
my_screen = Screen()
y = 250

all_turtle = []
all_turtle_colors = []
for i in range(len(colors_list)):
    timmy = Turtle()
    timmy.color(colors_list[i])
    timmy.shape('turtle')
    my_screen.setup(height=800, width=1000)
    timmy.penup()
    timmy.goto(x=-470,y = y)
    y-=50
    line = timmy.pencolor()
    all_turtle_colors.append(line)
    all_turtle.append(timmy)
answer = False
while answer == False:
    bet = my_screen.textinput(
        "Turtle race", "On which turtle would you bet? Guess a color: "
    )
    if bet not in all_turtle_colors:
        print("the color you have entered is not available")
    if bet in all_turtle_colors:
        answer = True
    

if bet:
    is_race_on = True

while is_race_on:
    for x in all_turtle:
        if x.xcor() > 480:
            win_color = x.pencolor()
            if win_color == bet:
                print(f"You've won! The {win_color} turtle is the winner")
            
            else:
                print(f"You've lost! The {win_color} turtle is the winner")

            is_race_on = False
        else:
            x.fd(random.randint(1,10))
    

    


my_screen.exitonclick()
