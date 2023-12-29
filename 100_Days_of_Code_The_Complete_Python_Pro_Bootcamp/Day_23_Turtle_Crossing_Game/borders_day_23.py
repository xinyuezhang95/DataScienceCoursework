# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 11:40:46 2023

@author: zxy23

Day 23: Create the Borders
"""

from turtle import Turtle

class Borders(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(600, 380)
        self.pendown()
        self.goto(600, -380)
        self.goto(-600, -380)
        self.goto(-600, 380)
        self.goto(600, 380)
        self.goto(600, -330)
        self.setheading(180)
        for _ in range(60):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
        self.penup()
        self.goto(-600, 330)
        self.setheading(0)
        for _ in range(60):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
