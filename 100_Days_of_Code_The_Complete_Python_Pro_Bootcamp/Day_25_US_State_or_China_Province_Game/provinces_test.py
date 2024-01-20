# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 16:29:28 2024

@author: zxy23
"""

import turtle
import pandas as pd

def display_name(province_name, province_x, province_y):
    province_display = turtle.Turtle()
    province_display.hideturtle()
    province_display.color('black')
    province_display.penup()
    province_display.goto(province_x, province_y)
    province_display.write(province_name)

screen = turtle.Screen()
screen.setup(width = 1000, height = 900)
screen.title('China Provinces Game')
image = 'China.gif'
screen.addshape(image)

turtle.shape(image)

provinces = pd.read_csv('23_provinces.csv')
all_provinces = provinces.province.to_list()

guessed_provinces = []

while len(guessed_provinces) < 34:
    answer_province = screen.textinput(title = f'{len(guessed_provinces)}/34 Provinces & Cities Correct', prompt = "What's another province's name?").title()
    
    if answer_province == 'Exit':
        missing_provinces = [province for province in all_provinces if province not in guessed_provinces]
        new_data = pd.DataFrame(missing_provinces)
        new_data.to_csv('provinces_to_learn.csv')
        break
    if (answer_province in all_provinces) and (answer_province not in guessed_provinces):
        input_province = provinces[provinces['province'] == answer_province]
        display_name(answer_province, int(input_province.x), int(input_province.y))
        guessed_provinces.append(answer_province)
            
screen.exitonclick()