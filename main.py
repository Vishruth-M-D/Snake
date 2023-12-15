from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=700)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15 :
        food.new_food()
        scoreboard.increase_score()
        snake.grow()

    # detect collision with wall :
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 340 or snake.head.ycor() < -350:
        is_game_on = False
        scoreboard.game_over()

    # detect collision with the snakes body itself

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_over = False
            scoreboard.game_over()

screen.exitonclick()