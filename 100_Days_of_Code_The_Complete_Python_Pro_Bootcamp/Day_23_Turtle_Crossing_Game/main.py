# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 11:35:46 2023

@author: zxy23

Day 23: Create the Turtle Crossing Game
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from borders_day_23 import Borders

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()

player = Player()

scoreboard = Scoreboard()

borders = Borders()

screen.listen()
screen.onkey(key = 'Up', fun = player.up)

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            scoreboard.game_over()
    
    # detect a successful crossing
    if player.reach_finish_line():
        player.go_to_start()
        scoreboard.level_up()
        car_manager.speed_up()
    
    # detect collision with cars
    #if player.head.xcor() > 580 or snake.head.xcor() < -580 or snake.head.ycor() > 370 or snake.head.ycor() < -370:
      #  is_game_on = False
      #  score_board.game_over()


screen.exitonclick()