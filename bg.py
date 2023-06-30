from turtle import Turtle

CENTER = (0, 0)


class Background(Turtle):
    def __int__(self):
        super().__init__()

    def center_lines(self):
        tim = Turtle()
        tim.shape("square")
        tim.penup()
        tim.color("white")
        tim.shapesize(stretch_wid=5, stretch_len=1)
        tim.goto(CENTER)
