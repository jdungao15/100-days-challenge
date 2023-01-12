from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card ={}
to_learn = {}
# -----------------DATA----------------
try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv('data/tagalog_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = df.to_dict(orient='records')





def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    random_tagalog_word = current_card['Tagalog']
    card.itemconfigure(card_title, text='Tagalog', fill='black')
    card.itemconfig(card_word, text=random_tagalog_word, fill='black')
    card.itemconfig(card_image, image=card_front_img)
    flip_timer= window.after(3000, flip_card)


def flip_card():
    card.itemconfig(card_title, text='English', fill='white')
    card.itemconfig(card_word, text=current_card['English'], fill='white')
    card.itemconfig(card_image, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

# -------------------UI SETUP --------------------------------
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='./images/card_back.png')

# Canvas
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = card.create_image(400, 263, image=card_front_img)
card.grid(row=0, column=0, columnspan=2)

# Canvas Text
card_title = card.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
card_word = card.create_text(400, 263, text='Word', font=('Arial', 60, 'bold'))

# Button
correct_img = PhotoImage(file='./images/right.png')
known_button = Button(image=correct_img, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR,
                      command=is_known, cursor='hand2')
known_button.grid(row=1, column=1)

wrong_img = PhotoImage(file='./images/wrong.png')
unknown_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, command=next_card,
                        cursor='hand2')
unknown_button.grid(row=1, column=0)

next_card()



window.mainloop()
