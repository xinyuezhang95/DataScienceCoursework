# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 11:37:46 2023

@author: zxy23

Day 23: Create the Car Manager
"""
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        random_chance = random.randint(1, 6)
        # basically every 6th times, a new car is created
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(1, 2) 
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-315, 315)
            new_car.goto(600, random_y)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            if car.xcor() <= -600:
                car.clear()
            
    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
