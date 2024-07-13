from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def restart_game():
    print("Restarting game...")
    global game_is_on
    game_is_on = False
    screen.update()
    snake.reset()
    food.refresh()
    scoreboard.reset()
    game_loop()

def game_loop():
    global game_is_on
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Collision with food 
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()

        # Collision with tail
        for square in snake.squares[1:]:
            if snake.head.distance(square) < 10:
                game_is_on = False
                scoreboard.game_over()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) 

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(restart_game, "space")

game_loop()
screen.exitonclick()
