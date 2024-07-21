from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Left")
screen.onkey(snake.move_left, "Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_increase()
        snake.extend()

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290 :
        score.high_score_increase()
        snake.reset_snake()


    for segment in snake.new_segment:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            score.high_score_increase()
            snake.reset_snake()






























screen.exitonclick()
