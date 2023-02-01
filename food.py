from turtle import *
from random import randint
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.new_position()

    def new_position(self):
        newx = randint(-280, 280)
        newy = randint(-280, 280)
        self.goto(newx, newy)