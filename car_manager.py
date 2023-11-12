from turtle import Turtle
import random
from turtle import Screen

screen = Screen()

# COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_SHAPE = "square"


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.all_cars = []
        self.r = 0
        self.g = 0
        self.b = 0
        self.random_color = ()
        self.position_y = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_color(self):
        new_color = Screen()
        new_color.colormode(255)
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        self.random_color = (self.r, self.g, self.b)
        # Checks for White Cars
        if self.random_color == (255, 255, 255):
            self.generate_color()
        else:
            return self.random_color

    def add_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape=CAR_SHAPE)
            new_car.penup()
            new_car.turtlesize(stretch_wid=1, stretch_len=2, outline=0)
            new_car.color(self.generate_color())
            random_y = random.randint(-250, 250)
            # Alternate way to get colors using COLORS - COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
            # new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.back(self.car_speed)

    def level_speed(self):
        self.car_speed += MOVE_INCREMENT
        # print(self.car_speed)



