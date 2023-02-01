import time
from turtle import *
from snake import Snake
from food import Food
from scorebord import Scorebord
screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

screen.tracer(0)
snake = Snake()
food = Food()
score = Scorebord()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
game_on= True

while game_on is True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15 :
        snake.extend()
        food.new_position()
        score.add_score()
    if snake.head.xcor() >280 or snake.head.xcor() < -290 or snake.head.ycor() >280 or snake.head.ycor() <-280:
        game_on= False
        score.game_over()
    for seg in snake.segment[3:]:
        if snake.head.distance(seg)< 15:
            game_on=False
            score.game_over()



screen.exitonclick()