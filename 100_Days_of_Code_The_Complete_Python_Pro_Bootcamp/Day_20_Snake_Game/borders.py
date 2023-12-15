# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:43:27 2023

@author: zxy23

Day 20: Create the Borders
"""

from turtle import Turtle

class Borders(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(600, 380)
        self.pendown()
        self.goto(600, -380)
        self.goto(-600, -380)
        self.goto(-600, 380)
        self.goto(600, 380)