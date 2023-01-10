import tkinter

window = tkinter.Tk()
window.title("Mile to Kilometers Converter")
window.minsize(width=500, height=300)
FONT = ("Arial", 20, "normal")


def calculate():
    miles = int(miles_entry.get())
    kilometers = round(miles * 1.60, 2)
    result.config(text=kilometers)

# Label
miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

is_equal_to_label = tkinter.Label(text="is equal to", font=FONT)
is_equal_to_label.grid(row=1, column=0)

result = tkinter.Label(text="0", font=FONT)
result.grid(row=1, column=1)

km_label = tkinter.Label(text="Kilometers", font=FONT)
km_label.grid(row=1, column=2)

# Entry
miles_entry = tkinter.Entry(text="0")
miles_entry.grid(row=0, column=1)

# Button
calculate = tkinter.Button(text="Calculate", font=FONT, command=calculate)
calculate.grid(row=2, column=1)




window.mainloop()
