from turtle import Turtle, Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from score import Scoreboard

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Bear Pong Game")

screen.tracer(False)
paddle1 = Paddle(370, 0)
paddle2 = Paddle(-370, 0)
ball = Ball()
screen.update()
score1 = Scoreboard(100)
score2 = Scoreboard(-100)
screen.tracer(True)

screen.listen()
screen.onkey(paddle1.mov_for, "Up")
screen.onkey(paddle1.mov_bak, "Down")
screen.onkey(paddle2.mov_for, "i")
screen.onkey(paddle2.mov_bak, "k")


def reset():
    screen.tracer(False)
    paddle1.goto(x=370, y=0)
    paddle2.goto(x=-370, y=0)
    ball.goto(x=0, y=0)
    ball.sign_x *= -1
    screen.update()
    screen.tracer(True)


game_condition = True
speed = 0.1

while game_condition:
    sleep(speed)
    screen.update()
    ball.move()

    if ball.distance(paddle1) < 49 and ball.xcor() > 340:
        ball.hit()
        speed /= 1.2
    elif ball.distance(paddle2) < 49 and ball.xcor() < -340:
        ball.hit()
        speed /= 1.2
    elif ball.xcor() > 380:
        score2.scored()
        reset()
        speed = 0.1
    elif ball.xcor() < -380:
        score1.scored()
        reset()
        speed = 0.1

screen.exitonclick()
