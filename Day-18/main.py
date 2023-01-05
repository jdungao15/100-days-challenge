import turtle
from turtle import Turtle, Screen

tim = Turtle()
import random


for _ in range(200):
    colors = ["#F0F8FF", "#FAEBD7", "#00FFFF", "#7FFFD4", "#F0FFFF", "#F5F5DC", "#FFE4C4", "#000000", "#FFEBCD",
              "#0000FF", "#8A2BE2", "#A52A2A", "#DEB887", "#5F9EA0", "#7FFF00", "#D2691E", "#FF7F50", "#6495ED",
              "#FFF8DC", "#DC143C"]
    angles = [0, 90, 180, 270]
    turtle.speed("fastest")
    tim.pensize(15)
    tim.color(random.choice(colors))
    tim.setheading(random.choice(angles))
    tim.forward(30)



screen = Screen()
screen.exitonclick()
