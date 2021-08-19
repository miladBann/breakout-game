from turtle import Turtle
import random

car_colors = ["red", "orange", "yellow", "green", "blue", "purple"]


class Object(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.space = 0
        self.current_X = -560
        self.current_Y = 270

    def create_first_row(self):
        for new_car in range(19):
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(car_colors))
            new_car.penup()
            new_car.shapesize(stretch_len=3, stretch_wid=1.25)
            new_car.goto(self.current_X + self.space, 270)
            self.space += 62
            self.all_cars.append(new_car)
        self.space = 0

    def create_second_row(self):
        for new_car in range(19):
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(car_colors))
            new_car.penup()
            new_car.shapesize(stretch_len=3, stretch_wid=1.25)
            new_car.goto(self.current_X + self.space, 243)
            self.space += 62
            self.all_cars.append(new_car)
        self.space = 0

    def create_third_row(self):
        for new_car in range(19):
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(car_colors))
            new_car.penup()
            new_car.shapesize(stretch_len=3, stretch_wid=1.25)
            new_car.goto(self.current_X + self.space, 216)
            self.space += 62
            self.all_cars.append(new_car)
        self.space = 0

    def create_fourth_row(self):
        for new_car in range(19):
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(car_colors))
            new_car.penup()
            new_car.shapesize(stretch_len=3, stretch_wid=1.25)
            new_car.goto(self.current_X + self.space, 189)
            self.space += 62
            self.all_cars.append(new_car)
        self.space = 0

    def create_fifth_row(self):
        for new_car in range(19):
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(car_colors))
            new_car.penup()
            new_car.shapesize(stretch_len=3, stretch_wid=1.25)
            new_car.goto(self.current_X + self.space, 162)
            self.space += 62
            self.all_cars.append(new_car)
        self.space = 0

    def create_sixth_row(self):
        for new_car in range(19):
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(car_colors))
            new_car.penup()
            new_car.shapesize(stretch_len=3, stretch_wid=1.25)
            new_car.goto(self.current_X + self.space, 135)
            self.space += 62
            self.all_cars.append(new_car)
        self.space = 0
