import time
import turtle
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Import names
score = Scoreboard()
player = Player()
car_mgr = CarManager()

# Keyboard Listen config
screen.listen()
screen.onkey(player.up, key="Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car_mgr.add_cars()
    car_mgr.move_cars()

    if player.ycor() > 280:
        score.level += 1
        player.restart_player()
        car_mgr.level_speed()
        score.score_level()

    for car in car_mgr.all_cars:
        if car.distance(player) < 20:
            # print("HIT")
            game_is_on = False
            score.game_over()

    screen.update()

screen.exitonclick()
