from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.sign_x = 1
        self.sign_y = 1

    def move(self):
        self.goto(self.xcor() + self.sign_x * 10, self.ycor() + self.sign_y * 10)
        if self.ycor() > 280 or self.ycor() < -280:
            self.sign_y *= -1

    def hit(self):
        self.sign_x *= -1
