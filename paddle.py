from turtle import *


class Paddle(Turtle):
    def __init__(self, destination):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=10)
        self.goto(destination)

    def move_right(self):
        self.forward(15)

    def move_left(self):
        self.back(15)
