# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:12:38 2023

@author: zxy23

Day 22: Create the Borders
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
        self.goto(0, 380)
        self.setheading(270)
        for _ in range(38):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()