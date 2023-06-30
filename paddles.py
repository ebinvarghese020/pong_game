from turtle import Turtle

MOVE = 20
BOUNDARY = 260


class Paddle:
    def __init__(self):
        self.tim = None

    def line(self, position):
        self.tim = Turtle()
        self.tim.shape("square")
        self.tim.color("white")
        self.tim.shapesize(stretch_len=1, stretch_wid=5)
        self.tim.penup()
        self.tim.goto(position)

    def up(self):
        if self.tim.ycor() < BOUNDARY:
            y = self.tim.ycor() + MOVE
            self.tim.goto(self.tim.xcor(), y)

    def down(self):
        if self.tim.ycor() > -BOUNDARY:
            y = self.tim.ycor() - MOVE
            self.tim.goto(self.tim.xcor(), y)
