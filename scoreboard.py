from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_POSITION = (-280, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(LEVEL_POSITION)
        self.level = 1
        self.write(f"Level {self.level}", align="left", font=FONT)

    def score_level(self):
        # self.level += 1
        self.clear()
        self.write(f"Level {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)




