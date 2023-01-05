import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
turtle.colormode(255)

rgb_colors = [(230, 215, 101), (234, 246, 242), (154, 80, 38), (244, 231, 236),
              (207, 159, 105), (181, 175, 18), (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105),
              (13, 37, 97), (72, 43, 23), (50, 121, 23), (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75),
              (25, 97, 25), (100, 120, 169), (180, 206, 170), (250, 169, 173), (24, 53, 110), (251, 171, 163),
              (149, 191, 244), (104, 60, 18), (81, 30, 46), (132, 79, 90), (18, 75, 105)]


def draw_hist_painting(size=20, row=10, col=10):
    x_cor = -225
    y_cor = -225
    t.penup()
    t.setposition(x_cor, y_cor)
    t.pendown()

    for _ in range(row):
        for _ in range(col):
            t.dot(size, random.choice(rgb_colors))
            t.penup()
            t.forward(50)
            t.pendown()
        t.penup()
        y_cor += 50
        t.setpos(x_cor, y_cor)
    t.hideturtle()


draw_hist_painting()

screen = Screen()
screen.exitonclick()
