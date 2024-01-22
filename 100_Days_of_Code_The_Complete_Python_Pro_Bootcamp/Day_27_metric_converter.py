# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 19:00:00 2024

@author: zxy23
"""

import tkinter 

def convert_metrics(number_input):
    if metric_label_1['text'] == 'Celcius':
        result = number_input * 9/5 + 32
    elif metric_label_1['text'] == 'Fahrenheit':
        result = (number_input - 32) * 5/9
    elif metric_label_1['text'] == 'Pounds':
        if metric_label_2['text'] == 'Oz':
            result = number_input * 16
        elif metric_label_2['text'] == 'Kg':
            result = number_input / 2.205
    elif metric_label_1['text'] == 'Oz':
        if metric_label_2['text'] == 'Pounds':
            result = number_input / 16
        elif metric_label_2['text'] == 'Kg':
            result = number_input / 35.274
    elif metric_label_1['text'] == 'Kg':
        if metric_label_2['text'] == 'Pounds':
            result = number_input * 2.205
        elif metric_label_2['text'] == 'Oz':
            result = number_input * 35.274
    elif metric_label_1['text'] == 'Miles':
        if metric_label_2['text'] == 'Km':
            result = number_input * 1.609
        elif metric_label_2['text'] == 'Feet':
            result = number_input * 5280
    elif metric_label_1['text'] == 'Km':
        if metric_label_2['text'] == 'Miles':
            result = number_input / 1.609
        elif metric_label_2['text'] == 'Feet':
            result = number_input * 3280
    elif metric_label_1['text'] == 'Feet':
        if metric_label_2['text'] == 'Km':
            result = number_input / 3280
        elif metric_label_2['text'] == 'Miles':
            result = number_input / 5280
    
    return round(result, 2)


def calc_button_clicked():
    number_input = int(num_input.get())
    output_label.config(text = convert_metrics(number_input))

def switch_button_clicked():
    metric_1 = metric_label_1['text']
    metric_label_1.config(text = metric_label_2['text'])
    metric_label_2.config(text = metric_1)

def listbox_used(event):
    # Gets current selection from listbox
    user_select = listbox.get(listbox.curselection())
    metric_1 = user_select.split('-')[0].strip()
    metric_2 = user_select.split('-')[1].strip()
    metric_label_1.config(text = metric_1)
    metric_label_2.config(text = metric_2)


window = tkinter.Tk()
window.title("Metric Converter")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

# Listbox
listbox = tkinter.Listbox(height = 7)
metrics = ['Celcius - Fahrenheit', 'Pounds - Kg', 'Pounds - Oz', 'Kg - Oz', 'Miles - Km', 'Km - Feet', 'Miles - Feet']
for item in metrics:
    listbox.insert(metrics.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column = 1, row = 0)

# Entry
num_input = tkinter.Entry(width = 30)
num_input.grid(column = 1, row = 1, ipady = 3)

# Label: first metric
metric_label_1 = tkinter.Label(text = "Miles", font=("Arial", 24))
metric_label_1.grid(column = 2, row = 1)

# Label: is equal to label
equal_label = tkinter.Label(text = "is equal to", font=("Arial", 24))
equal_label.grid(column = 0, row = 2)

# Label: second metric
metric_label_2 = tkinter.Label(text = "Km", font=("Arial", 24))
metric_label_2.grid(column = 2, row = 2)

# Label: output 
output_label = tkinter.Label(text = 0, font=("Arial", 24))
output_label.grid(column = 1, row = 2)

# Buttons
calc_button = tkinter.Button(text = "Calculate", command = calc_button_clicked)
calc_button.grid(column = 1, row = 3)

switch_button = tkinter.Button(text = "Switch Metrics", command = switch_button_clicked)
switch_button.grid(column = 0, row = 3)



window.mainloop()