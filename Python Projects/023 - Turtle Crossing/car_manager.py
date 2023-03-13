import random
from turtle import Turtle
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
DIFFICULTY = 6  # LOWER IS HIGHER DIFFICULTY


class CarManager():
    def __init__(self):
        self.cars = []

    def create_car(self):
        random_car = random.randint(1, DIFFICULTY)
        if random_car == DIFFICULTY:
            new_car = Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(stretch_len=2)
            new_car.goto(x=300, y=random.randint(-250, 250))
            self.cars.append(new_car)

    def car_moving(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)
