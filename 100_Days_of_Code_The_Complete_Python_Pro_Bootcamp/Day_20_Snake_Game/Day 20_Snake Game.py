# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:29:48 2023

@author: zxy23

Day 20: Snake Game
"""
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from borders import Borders
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# set up the snake
snake = Snake()
food = Food()
score_board = Scoreboard()
borders = Borders()

screen.listen()
screen.onkey(key = 'Up', fun = snake.up)
screen.onkey(key = 'Down', fun = snake.down)
screen.onkey(key = 'Left', fun = snake.left)
screen.onkey(key = 'Right', fun = snake.right)

is_game_on = True

while is_game_on:
    screen.update()
    # use timer to delay the refresh
    time.sleep(0.1)
    
    snake.move()
    
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.update_score()
    
    # detect collision with wall
    if snake.head.xcor() > 580 or snake.head.xcor() < -580 or snake.head.ycor() > 370 or snake.head.ycor() < -370:
        is_game_on = False
        score_board.game_over()
        
    # detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score_board.game_over()
    
screen.exitonclick()
