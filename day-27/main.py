import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="New Text", font=('Arial', 24, 'bold'))
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=30)


# Label


# Button

def button_click():
    my_label.config(text=input.get())


button = tkinter.Button(text='Click me', command=button_click)
button.grid(row=1, column=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(row=0, column=2)

# Entry
input = tkinter.Entry(width=10)
input.grid(row=2, column=3)

window.mainloop()
