# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 22:45:46 2023

@author: zxy23
"""

import turtle
import pandas as pd

def display_name(state_name, state_x, state_y):
    state_display = turtle.Turtle()
    state_display.hideturtle()
    state_display.color('black')
    state_display.penup()
    state_display.goto(state_x, state_y)
    state_display.write(state_name)

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

states = pd.read_csv('50_states.csv')
all_states = states.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f'{len(guessed_states)}/50 States Correct', prompt = "What's another state's name?").title()
    
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    
    if (answer_state in all_states) and (answer_state not in guessed_states):
        input_state = states[states['state'] == answer_state]
        display_name(answer_state, int(input_state.x), int(input_state.y))
        guessed_states.append(answer_state)
            
screen.exitonclick()