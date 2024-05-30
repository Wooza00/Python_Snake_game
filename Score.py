from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Gothic", 12, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.setposition(0, 280)
        self.new_score()

    def new_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.clear()
        self.score += 1
        self.new_score()
