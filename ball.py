from turtle import Turtle


class Ball:
    def __init__(self):
        self.tim = Turtle()
        self.tim.color("white")
        self.tim.shape("circle")
        self.tim.penup()
        self.x_move = 10
        self.y_move = 10
        self.motion_speed = 0.1

    def move(self):
        x = self.tim.xcor() + self.x_move
        y = self.tim.ycor() + self.y_move
        self.tim.goto(x, y)

    def boundary(self):
        self.y_move *= -1
        self.motion_speed *= 0.9

    def bounce(self):
        self.x_move *= -1
        self.motion_speed *= 0.9

    def reset(self):
        self.tim.goto(0, 0)
        self.bounce()
        self.motion_speed = 0.1