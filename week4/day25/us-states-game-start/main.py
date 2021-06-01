import pandas
from turtle import Turtle, Screen
import turtle as t
import time

my_screen = Screen()
my_screen.bgpic("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
total_states = len(states)
ans_states = 0
correct_ans_state = []
while ans_states != total_states:
    input_state = my_screen.textinput(f"{ans_states}/{total_states}States correct", "What's another state's name").title()
    if input_state == 'Exit':
        break
    if input_state in states:
        correct_ans_state.append(input_state)
        correct_state = Turtle()
        correct_state.hideturtle()
        correct_state.penup()
        write_data = data[data.state == input_state]
        correct_state.goto(int(write_data.x), int(write_data.y))
        correct_state.write(f"{input_state}", align="center", font=("Arial", 15, "normal"))
        ans_states+=1
    
states_to_learn = [ids for ids in states if ids not in correct_ans_state]
df = pandas.DataFrame(states_to_learn)
df.to_csv("states_learn.csv")




# my_screen.mainloop()
