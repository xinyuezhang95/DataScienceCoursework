# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:32:26 2023

@author: zxy23

Day 20: Create the Scoreboard class
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
        self.goto(0, 350)
        self.score = 0
        self.read_high_score()
        self.display_score()
        
    def read_high_score(self):
        with open('snake_game_high_score.txt') as file:
            self.high_score = int(file.read())

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)
        
    def update_score(self):
        self.score += 1
        self.display_score()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('snake_game_high_score.txt', mode = 'w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.display_score()
        
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align = ALIGNMENT, font = FONT)