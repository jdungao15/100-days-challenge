from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
# -----------------DATA----------------
df = pd.read_csv("./data/french_words.csv")
french_data = df.to_dict(orient='records')


def random_word():
    french_word = random.choice(french_data)
    print(french_word)
    random_french_word = french_word['French']
    card_front.itemconfig(card_front_text, text=random_french_word)


# -------------------UI SETUP --------------------------------
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
card_front = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='./images/card_front.png')
card_front.create_image(400, 263, image=card_front_img)
card_front.grid(row=0, column=0, columnspan=2)

card_back =  Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file='./images/card_back.png')
card_back.create_image(400, 263, image=card_back_img)
card_back.grid(row=0, column=0, columnspan=2)

# Canvas Text
card_front.create_text(400, 150, text='French', font=('Ariel', 40, 'italic'))
card_front_text = card_front.create_text(400, 263, text='trouve', font=('Arial', 60, 'bold'))

card_back.create_text(400, 150, text='English', font=('Arial',40, 'italic'))
card_back_text = card_front.create_text(400, 263, text='trouve', font=('Arial', 60, 'bold'))
# Button
correct_img = PhotoImage(file='./images/right.png')
correct_button = Button(image=correct_img, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR,
                        command=random_word, cursor='hand2')
correct_button.grid(row=1, column=0)

wrong_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, command=random_word,
                      cursor='hand2')
wrong_button.grid(row=1, column=1)

window.mainloop()
