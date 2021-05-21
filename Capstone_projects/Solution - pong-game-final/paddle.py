from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position , color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor()< 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
        else:
            pass

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
        else:
            pass
