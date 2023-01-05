import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.speed(0)
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
#
# for _ in range(1000):
#     angles = [0, 90, 180, 270]
#     turtle.speed("fastest")
#     tim.pensize(15)
#     tim.color(random_color())
#     tim.setheading(random.choice(angles))
#     tim.forward(30)
draw_spirograph(5)


screen = Screen()
screen.exitonclick()
