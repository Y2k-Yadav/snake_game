from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 15, "bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0,275)
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score} ", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_score()


