from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = Label(text='Score', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text='Text Here',
                                                     font=('Arial', 20, 'italic'))

        # Button
        true_button_img = PhotoImage(file='images/true.png')
        false_button_img = PhotoImage(file='images/false.png')

        self.true_button = Button(image=true_button_img, highlightthickness=0, borderwidth=0, command=self.true_button_clicked)
        self.false_button = Button(image=false_button_img, highlightthickness=0, borderwidth=0, command=self.false_button_clicked)
        self.true_button.grid(row=2, column=0, pady=(25, 10))
        self.false_button.grid(row=2, column=1, pady=(25, 10))

        self.get_next_questions()
        self.window.mainloop()

    def get_next_questions(self):
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz.')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
        self.canvas.config(bg='white')


    def true_button_clicked(self):
        is_right = self.quiz.check_answer('True')
        self.get_feedback(is_right)

    def false_button_clicked(self):
        is_wrong = self.quiz.check_answer('False')
        self.get_feedback(is_wrong)


    def get_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')

        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_questions)

