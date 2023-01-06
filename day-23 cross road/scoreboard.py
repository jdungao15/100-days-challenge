from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.penup()
        self.goto(-270, 250)
        self.hideturtle()
        self.write(f"Level {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)