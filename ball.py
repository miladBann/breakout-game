from turtle import *


class Ball(Turtle):
    def __init__(self, destination):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(destination)
        self.move_x = 10
        self.move_y = 10

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def reflect_sides(self):
        self.move_x *= -1

    def reflect_up_down(self):
        self.move_y *= -1
