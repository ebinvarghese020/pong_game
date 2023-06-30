from turtle import Turtle

FONT_ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.arg = "Score  "
        self.left = 0
        self.right = 0
        self.scoreboard()

    def scoreboard(self):
        self.color("white")
        self.penup()
        self.hideturtle()

        self.goto(10, 270)
        self.write(self.arg, move=False, align=FONT_ALIGN, font=FONT)

        self.goto(10, 250)
        self.write(self.left, move=False, align=FONT_ALIGN, font=FONT)
        self.goto(-20, 250)
        self.write(self.right, move=False, align=FONT_ALIGN, font=FONT)

    def left_score(self):
        self.left += 1
        self.clear()
        self.scoreboard()


    def right_score(self):
        self.right += 1
        self.clear()
        self.scoreboard()
