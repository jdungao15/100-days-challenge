from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
import json


# Search Functionality
def find_password():
    user_email = username_entry.get()
    user_website = website_entry.get()
    # Check if data exist
    try:
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No Data File Found")
    else:
        # If data exist, check if website exist
        try:
            user_data = data[website_entry.get().title()]
        except KeyError:
            messagebox.showerror("Error", "No details for the website exists")
        else:



            # check if email exist
            if user_email not in user_data.values():
                messagebox.showerror("Error", "Email Not Found")
            else:
                password = user_data['password']
                messagebox.showinfo(user_website, f"Email: {user_email}\nPassword: {password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
alphabet_and_char = list(string.ascii_lowercase + string.ascii_uppercase + string.punctuation)


def generate_password():
    password = ""
    password_entry.delete(0, END)
    for i in range(15):
        password += random.choice(alphabet_and_char)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get().title()
    password = password_entry.get()
    email = username_entry.get()
    new_data = {website:
        {
            "email": email,
            "password": password
        }
    }
    # check if entry field is empty
    if website == "" or password == "" or email == "":
        messagebox.showerror("Error", "Please fill in all the fields")
    else:
        try:
            with open('data.json', 'r') as password_file:
                # Read Old Data
                data = json.load(password_file)
        except FileNotFoundError:
            with open('data.json', 'w') as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            with open('data.json', 'w') as password_file:
                # Update Old Data
                data.update(new_data)
                # Write New Data
                json.dump(data, password_file, indent=4)
        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)
            pyperclip.copy(f"{website} | {email} | {password}")


# ---------------------------- UI SETUP ---------- --------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Password Manager Logo

# Insert Image in Frame
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

username_label = Label(text='Email/Username:')
username_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entry Box
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=1, sticky='EW')
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky='EW')
username_entry.insert(0, "jdungao3342@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='EW')

# Buttons
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2, padx=(5, 0))

search_button = Button(text='Search', command=find_password)
search_button.grid(row=1, column=2, sticky='EW', padx=(5, 0))

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

# copy to clipboard


window.mainloop()
