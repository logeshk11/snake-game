from turtle import Turtle

class Scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.score=-1
        self.add_score()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.pencolor("White")
        self.add_score()
    def add_score(self):
        self.clear()
        self.write(f"score:{self.score}", move=False, align='center', font=("Arial", 16, "normal"))
        self.score+=1
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align='center', font=("Arial", 16, "normal"))
