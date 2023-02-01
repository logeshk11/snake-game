
from turtle import Turtle

STARTING_POSITION =[(0,0), (20,0), (40,0)]
class Snake:

    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head= self.segment[0]
    def create_snake(self):
        for pos in STARTING_POSITION:
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.goto(pos)
            self.segment.append(snake)

    def add_segment(self, position):
       snake = Turtle()
       snake.shape("square")
       snake.color("white")
       snake.penup()
       snake.goto(position)
       self.segment.append(snake)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            newx = self.segment[seg - 1].xcor()
            newy = self.segment[seg - 1].ycor()
            self.segment[seg].goto(newx, newy)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)