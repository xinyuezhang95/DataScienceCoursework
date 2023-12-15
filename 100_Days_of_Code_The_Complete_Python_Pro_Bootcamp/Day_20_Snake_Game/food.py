# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:36:54 2023

@author: zxy23

Day 20: Create the Food class
"""

from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(-550, 550)
        random_y = random.randint(-300, 300)
        self.goto(random_x, random_y)
        
