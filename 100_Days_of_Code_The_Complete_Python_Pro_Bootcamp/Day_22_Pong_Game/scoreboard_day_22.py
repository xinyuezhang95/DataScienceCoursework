# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:13:21 2023

@author: zxy23

Day 22: Create the Scoreboard class
"""

from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-20, 350)
        self.write(self.l_score, align = ALIGNMENT, font = FONT)
        self.goto(20, 350)
        self.write(self.r_score, align = ALIGNMENT, font = FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align = ALIGNMENT, font = FONT)
        
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
        
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()