from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(1, 5, 1)
        self.setheading(90)
        self.goto(x=x, y=y)

    def mov_for(self):
        self.forward(30)

    def mov_bak(self):
        self.backward(30)
