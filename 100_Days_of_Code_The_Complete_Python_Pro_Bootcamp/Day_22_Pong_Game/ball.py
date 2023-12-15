# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 23:33:29 2023

@author: zxy23

Day 20: Create the Ball class
"""

from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_movement = 10
        self.y_movement = 10
        self.move_speed = 0.08
        
    def move(self):
        if self.ycor() >= 370 or self.ycor() <= -370:
            self.y_movement *= -1
            
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)
        
    def bounce(self):
        self.x_movement *= -1
        self.move_speed *= 0.9
        
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce()
        