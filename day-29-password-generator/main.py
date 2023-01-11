from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    password = password_entry.get()
    email = username_entry.get()

    with open('data.txt', 'a') as password_file:
        password_file.write(f"{website} | {email} | {password} \n")

    password_entry.delete(0, END)
    website_entry.delete(0, END)

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
generate_button = Button(text='Generate Password')
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

window.mainloop()
