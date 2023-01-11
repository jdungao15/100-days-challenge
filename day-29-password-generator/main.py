from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
alphabet_and_char = list(string.ascii_lowercase + string.ascii_uppercase + string.punctuation)
def generate_password():
    password = ""
    password_entry.delete(0, END)
    for i in range(15):
        password += random.choice(alphabet_and_char)
    password = [char for char in alphabet_and_char ]
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    password = password_entry.get()
    email = username_entry.get()

    #check if entry field is empty
    if website == "" or password == "" or email == "":
        messagebox.showerror("Error", "Please fill in all the fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} "
                                                      f"\n Password: {password} \n is it okay to save?")
        if is_ok:
            with open('data.txt', 'a') as password_file:
                password_file.write(f"{website} | {email} | {password} \n")
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
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky='EW')
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky='EW')
username_entry.insert(0, "jdungao3342@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='EW')

# Buttons
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

#copy to clipboard


window.mainloop()
