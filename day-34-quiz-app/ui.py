THEME_COLOR = "#375362"
from tkinter import *


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = Label(text='Score', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.quiz_text = self.canvas.create_text(150, 125, text='Text Here', font=('Arial', 20, 'italic'))

        # Button
        true_button_img = PhotoImage(file='images/true.png')
        false_button_img = PhotoImage(file='images/false.png')

        self.true_button_img = Button(image=true_button_img, highlightthickness=0, borderwidth=0)
        self.false_button_img = Button(image=false_button_img, highlightthickness=0, borderwidth=0)
        self.true_button_img.grid(row=2, column=0, pady=(25, 10))
        self.false_button_img.grid(row=2, column=1, pady=(25, 10))

        self.window.mainloop()
