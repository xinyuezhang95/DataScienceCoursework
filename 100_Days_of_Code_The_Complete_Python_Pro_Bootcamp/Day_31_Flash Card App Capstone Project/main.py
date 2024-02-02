import tkinter 
import pandas as pd
from random import choice

BACKGROUND_COLOR = '#B1DDC6'
FONT_NAME = 'Ariel'


# ---------------------------- Functions ------------------------------------ #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(title_text, text = 'Japanese', fill = 'black')
    canvas.itemconfig(word_text, text = current_card['Japanese'], fill = 'black')
    canvas.itemconfig(pron_text, text = '')
    canvas.itemconfigure(card_background, image = card_front_img)
    flip_timer = window.after(3000, func = show_pron)

def add_progress():
    global is_known, num_known_words
    if is_known:
        print(is_known)
        if current_card not in is_known:
            is_known.append(current_card)
    else:
        is_known = [current_card]
    
    is_known_df = pd.DataFrame(is_known)
    is_known_df.to_csv('data/known_words.csv', index = False)
    num_known_words = len(is_known)
            
    progress_label.config(text = f"Progress: {num_known_words}/{num_of_words}")
    next_card()
    

def show_pron():
    canvas.itemconfig(pron_text, text = current_card['Pronunciation'])

def flip_card():
    if canvas.itemcget(title_text, 'text') == 'Japanese':
        canvas.itemconfig(title_text, text = 'English', fill = 'white')
        canvas.itemconfig(word_text, text = current_card['English'], fill = 'white', width = 800)
        canvas.itemconfig(pron_text, text = '')
        canvas.itemconfigure(card_background, image = card_back_img)
    else:
        canvas.itemconfig(title_text, text = 'Japanese', fill = 'black')
        canvas.itemconfig(word_text, text = current_card['Japanese'], fill = 'black')
        canvas.itemconfig(pron_text, text = current_card['Pronunciation'])
        canvas.itemconfigure(card_background, image = card_front_img)
    
    
# ---------------------------- PICK WORDS ------------------------------- #
japanese_words = pd.read_csv('data/japanese_words.csv')
num_of_words = len(japanese_words)
to_learn = japanese_words.to_dict(orient = 'records')
current_card = {}

# ---------------------------- CHECK PROGRESS ------------------------------- #
try:
    with open('data/known_words.csv', 'r') as known_words_file:
        known_words = pd.read_csv('data/known_words.csv')
        is_known = known_words.to_dict(orient = 'records')
        num_known_words = len(is_known)
        print(is_known)
except FileNotFoundError:
    is_known = []
    num_known_words = 0

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Flashy')
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func = show_pron)

# canvas: display the image
canvas = tkinter.Canvas(width = 800, height = 426, bg = BACKGROUND_COLOR, highlightthickness = 0)
card_front_img = tkinter.PhotoImage(file = 'images/card_front.png')
card_back_img = tkinter.PhotoImage(file = 'images/card_back.png')
card_background = canvas.create_image(400, 213, image = card_front_img)

# display the text
title_text = canvas.create_text(400, 80, text = '', font = (FONT_NAME, 30, 'italic'))
word_text = canvas.create_text(400, 213, text = '', font = (FONT_NAME, 55, 'bold'))
pron_text = canvas.create_text(400, 300, text = '', font = (FONT_NAME, 30))
canvas.grid(column = 0, columnspan = 3, row = 1)

# label: progress
progress_label = tkinter.Label(text = f"Progress: {num_known_words}/{num_of_words}", font = (FONT_NAME, 20))
progress_label.grid(column = 2, row = 0)

# three buttons: known button
right_image = tkinter.PhotoImage(file = 'images/right.png')
known_button = tkinter.Button(image = right_image, highlightthickness = 0, bg = BACKGROUND_COLOR, command = add_progress)
known_button.grid(column = 2, row = 2)

# three buttons: unknown button
wrong_image = tkinter.PhotoImage(file = 'images/wrong.png')
unknown_button = tkinter.Button(image = wrong_image, highlightthickness = 0, command = next_card)
unknown_button.grid(column = 0, row = 2)

# three buttons: flip button
flip_image = tkinter.PhotoImage(file = 'images/flip.png')
flip_button = tkinter.Button(image = flip_image, highlightthickness = 0, command = flip_card)
flip_button.grid(column = 1, row = 2)

next_card()

window.mainloop()