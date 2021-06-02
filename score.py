from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=x, y=200)
        self.color("white")
        self.write(self.score, align="center", font=("Courier", 80, "normal"))

    def scored(self):
        self.clear()
        self.score += 1
        self.write(self.score, align="center", font=("Courier", 80, "normal"))
