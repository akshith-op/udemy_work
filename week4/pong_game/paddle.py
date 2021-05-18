from turtle import Turtle, Screen
class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5,1)
        self.penup()
        self.goto(x = x_cor, y = 0)
    

