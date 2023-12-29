# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 22:35:52 2023

@author: zxy23

Project objective: create a letter using starting_letter.txt 
for each name in invited_names.txt.
Replace the [name] placeholder with the actual name.
Save the letters in the folder "ReadyToSend".
"""
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open('./Input/Names/invited_names.txt') as names:
    name_list = names.readlines()     

with open('./Input/Letters/starting_letter.txt') as letter:
    letter_content = letter.read()
    for n in name_list:
        name = n.strip()
        new_letter = letter_content.replace(PLACEHOLDER, name)
        with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode = 'w') as invitation:
            invitation.write(new_letter)

