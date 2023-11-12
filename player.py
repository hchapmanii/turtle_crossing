from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
# FINISH_LINE_Y = 280
SHAPE = "turtle"
ALIGN = 90


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.setheading(ALIGN)
        self.goto(STARTING_POSITION)
        self.new_y = self.ycor()

    def up(self):
        self.new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), self.new_y)

    def restart_player(self):
        self.goto(STARTING_POSITION)

