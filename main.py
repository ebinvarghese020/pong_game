import time
from turtle import Screen

from ball import Ball
from bg import Background
from paddles import Paddle
from score import Score

LEFT = (280, 0)
RIGHT = (-280, 0)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

score = Score()
# bg = Background()
# bg.center_lines()

ball = Ball()


left_paddle = Paddle()
left_paddle.line(LEFT)

screen.listen()
screen.onkey(left_paddle.up, "Up")
screen.onkey(left_paddle.down, "Down")

right_paddle = Paddle()
right_paddle.line(RIGHT)

screen.listen()
screen.onkey(right_paddle.up, "w")
screen.onkey(right_paddle.down, "s")

game = True
while game:
    time.sleep(ball.motion_speed)
    screen.update()
    ball.move()

    if ball.tim.ycor() > 280 or ball.tim.ycor() < -280 :
        ball.boundary()

    if (ball.tim.distance(left_paddle.tim) < 50 and ball.tim.xcor() > 240) or (ball.tim.distance(right_paddle.tim) < 50 and ball.tim.xcor() < -240):
        ball.bounce()

    if ball.tim.xcor() > 260 :
        ball.reset()
        score.right_score()

    if ball.tim.xcor() < -260:
        ball.reset()
        score.left_score()

screen.exitonclick()
