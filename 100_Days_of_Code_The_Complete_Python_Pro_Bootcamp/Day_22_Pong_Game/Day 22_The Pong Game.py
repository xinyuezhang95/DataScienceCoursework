# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:13:21 2023

@author: zxy23

Day 22: The Pong Game
"""

from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard_day_22 import Scoreboard
from borders_day_22 import Borders
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor('black')
screen.title('The Pong Game')
screen.tracer(0)

# set up two tablets, a ping-pong ball, and two scoreboards
l_paddle = Paddle((-550, 0))
r_paddle = Paddle((550, 0))

ball = Ball()

scoreboard = Scoreboard()

borders = Borders()

screen.listen()
screen.onkey(key = 'W', fun = l_paddle.up)
screen.onkey(key = 'S', fun = l_paddle.down)
screen.onkey(key = 'Up', fun = r_paddle.up)
screen.onkey(key = 'Down', fun = r_paddle.down)

is_game_on = True

while is_game_on:
    # use timer to delay the refresh
    time.sleep(ball.move_speed)
    
    screen.update()
    
    ball.move()
        
    # detect collision with paddles
    if ball.xcor() == 530 and ball.distance(r_paddle) < 50:
        scoreboard.r_point()
        ball.bounce()
        
    if ball.xcor() == -530 and ball.distance(l_paddle) < 50:
        scoreboard.l_point()
        ball.bounce()
        
    # detect if the paddles miss the ball
    if ball.xcor() >= 600:
        ball.reset_position()
        scoreboard.l_point()
        
    if ball.xcor() <= -600:
        ball.reset_position()
        scoreboard.r_point()
    
screen.exitonclick()
