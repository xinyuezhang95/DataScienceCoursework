# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 11:36:46 2023

@author: zxy23

Day 23: Create the player
"""

from turtle import Turtle

STARTING_POSITION = (0, -360)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 340


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        
    def up(self):
        self.forward(MOVE_DISTANCE)
        
    def reach_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)
