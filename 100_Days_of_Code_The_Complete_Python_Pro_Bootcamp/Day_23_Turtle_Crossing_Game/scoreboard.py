# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 11:38:46 2023

@author: zxy23

Day 22: Create the Scoreboard class
"""

from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-550, 330)
        self.write_scoreboard()
        
    def write_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align = 'left', font = FONT)
        
    def level_up(self):
        self.level += 1
        self.write_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align = 'center', font = FONT)