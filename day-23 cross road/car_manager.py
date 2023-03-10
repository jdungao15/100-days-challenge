import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.speed)

    def gen_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            y_cor = random.randint(-250, 250)
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(280, y_cor)
            self.all_cars.append(new_car)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
