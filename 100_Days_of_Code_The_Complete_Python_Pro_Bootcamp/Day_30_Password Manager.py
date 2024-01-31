import tkinter 
from random import choice, randint, shuffle
import pyperclip
import json

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pwd():
    # Password Generator Project
    password_letters = [choice(LETTERS) for _ in range(randint(6, 10))]
    password_numbers = [choice(NUMBERS) for _ in range(randint(1, 4))]
    password_symbols = [choice(SYMBOLS) for _ in range(randint(0, 4))]
    password_list = password_letters + password_numbers + password_symbols
    
    shuffle(password_list)
    password = ''.join(password_list)
    
    pwd_input.delete(0, tkinter.END)
    pwd_input.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = username_input.get()
    pwd = pwd_input.get()
    
    new_data = {
        website: {
            "email": email, 
            "password": pwd,
            }
        }
    
    if len(website) == 0 or len(pwd) == 0:
        tkinter.messagebox.showinfo(title = 'Oops', message = "Please don't leave any fields empty!")
    else:
        try:
            with open('password_manager.json', 'r') as pwd_file:
                # read existing data
                data = json.load(pwd_file)
                # update
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open('password_manager.json', 'w') as pwd_file:
                # save
                json.dump(data, pwd_file, indent = 4)
                
                website_input.delete(0, tkinter.END)
                pwd_input.delete(0, tkinter.END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    
    if len(website) == 0:
        tkinter.messagebox.showinfo(title = 'Oops', message = "Please search for a specific website.")
    else:
        try:
            with open('password_manager.json', 'r') as pwd_file:
                # read existing data
                data = json.load(pwd_file)
        except FileNotFoundError:
            tkinter.messagebox.showinfo(title = 'Oops', message = "No Data File Found.")
        else:
            if website in data:
                email = data[website]['email']
                pwd = data[website]['password']
                tkinter.messagebox.showinfo(title = website, message = f"Email: {email}\nPassword: {pwd}")
            else:
                tkinter.messagebox.showinfo(title = 'Oops', message = f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx = 50, pady = 50)

# first canvas; display the image
canvas = tkinter.Canvas(width = 200, height = 200)
tomato_img = tkinter.PhotoImage(file = 'logo.png')
canvas.create_image(100, 100, image = tomato_img)
canvas.grid(column = 1, row = 0)

# Label: website
website_label = tkinter.Label(text = "Website: ")
website_label.grid(column = 0, row = 1)

# Label: username
username_label = tkinter.Label(text = "Email/Username: ")
username_label.grid(column = 0, row = 2)

# Label: website
password_label = tkinter.Label(text = "Password: ")
password_label.grid(column = 0, row = 3)

# Entry: website
website_input = tkinter.Entry(width = 33)
website_input.grid(column = 1, row = 1)
website_input.focus()

# Entry: username
username_input = tkinter.Entry(width = 52)
username_input.grid(column = 1, columnspan = 2, row = 2)
username_input.insert(0, 'cherylzhang2021@gmail.com')

# Entry: password
pwd_input = tkinter.Entry(width = 33)
pwd_input.grid(column = 1, row = 3)

# Buttons: search
search_button = tkinter.Button(text = "Search", command = find_password, width = 15)
search_button.grid(column = 2, row = 1)

# Buttons: generate password
generate_button = tkinter.Button(text = "Generate Password", command = gen_pwd, width = 15)
generate_button.grid(column = 2, row = 3)

# Buttons: add
add_button = tkinter.Button(text = "Save", command = save, width = 45)
add_button.grid(row = 4, column = 1, columnspan = 2)

window.mainloop()