import tkinter 
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
PURPLE = "#A833FF"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = "#33C1FF"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_button_clicked():
    # stop the timer
    window.after_cancel(timer)
    # timer_text: 00:00
    canvas.itemconfig(timer_text, text = '00:00')
    # title_label: Timer
    title_label.config(text = 'Timer', fg = GREEN)
    # reset checkmarks
    global reps
    reps = 0
    checkmarks_label.config(text = '')
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if (reps % 8) in [1, 3, 5, 7]:
        title_label.config(text = 'Work', fg = PURPLE)
        count_down(work_sec)
    elif (reps % 8) in [2, 4, 6]:
        title_label.config(text = 'Break', fg = BLUE)
        count_down(short_break_sec)
    else:
        title_label.config(text = 'Break', fg = GREEN)
        count_down(long_break_sec)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    
    canvas.itemconfig(timer_text, text = f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks_label.config(text = "✔" * (reps // 2))
        
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx = 100, pady = 50, bg = YELLOW)

# first canvas; display the image
canvas = tkinter.Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = tkinter.PhotoImage(file = 'tomato.png')
canvas.create_image(100, 112, image = tomato_img)

# display the text
timer_text = canvas.create_text(100, 130, text = '00:00', fill = 'white', font = (FONT_NAME, 35, 'bold'))
canvas.grid(column = 1, row = 1)

# Label: the timer
title_label = tkinter.Label(text = "Timer", fg = GREEN, bg = YELLOW, font=(FONT_NAME, 50, 'bold'))
title_label.grid(column = 1, row = 0)

# Buttons: start
start_button = tkinter.Button(text = "Start", highlightthickness = 0, command = start_timer)
start_button.grid(column = 0, row = 2)

# Buttons: reset
reset_button = tkinter.Button(text = "Reset", highlightthickness = 0, command = reset_button_clicked)
reset_button.grid(column = 2, row = 2)

# Label: the check marks
checkmarks_label = tkinter.Label(fg = GREEN, bg = YELLOW)
checkmarks_label.grid(column = 1, row = 3)

window.mainloop()