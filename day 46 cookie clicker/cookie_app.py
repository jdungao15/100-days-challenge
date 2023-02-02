from tkinter import *
from cookie import Cookie
from threading import Thread


class CookieApp:

    def __init__(self):
        self.cookie = Cookie()
        self.start_click = False
        self.screen = Tk()
        self.screen.title("Cookie Clicker")

        # start

        # Open the image file and create a PhotoImage object
        self.background = PhotoImage(file="cookie.png")

        # Create a Label widget to display the image
        self.label = Label(self.screen, image=self.background)
        self.label.pack()

        # load button
        self.load_button = Button(text="Load Cookie", highlightthickness=0,
                                  command=lambda: Thread(target=self.cookie.upload_data).start())
        self.load_button.place(relx=0.04, rely=0.5, height=100, width=100)

        # save button
        self.save_button = Button(text="Save Cookie", highlightthickness=0,
                                  command=lambda: Thread(target=self.cookie.save_file).start())
        self.save_button.place(relx=0.8, rely=0.5, height=100, width=100)

        # Start Button
        self.start_button = Button(text="Start", highlightthickness=0,
                                   command=lambda: Thread(target=self.cookie.start).start())
        self.start_button.place(relx=0.04, rely=0.8, height=100, width=100)

        # Stop Button
        self.stop_button = Button(text="Stop", highlightthickness=0,
                                  command=lambda: Thread(target=self.cookie.stop).start())
        self.stop_button.place(relx=0.8, rely=0.8, height=100, width=100)

        self.screen.mainloop()
