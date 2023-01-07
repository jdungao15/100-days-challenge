import turtle
import pandas as pd

FONT = ('Arial', 8, 'normal')
screen = turtle.Screen()
screen.title("U.S States Game")
IMAGE = "blank_states_img.gif"
score = 0

screen.addshape(IMAGE)
turtle.shape(IMAGE)
name_writer = turtle.Turtle()
game_is_ready = True

state_data = pd.read_csv("50_states.csv")
state_list = state_data.state.to_list()
print(state_list)
while game_is_ready:
    answer_state = screen.textinput(title=f"{score}/50 Guess the states", prompt="What's another state's name")

    # check answer
    if answer_state.title() in state_list:
        state = state_data[state_data["state"] == answer_state.title()]
        state_name = state["state"].item()
        state_x = state["x"].item()
        state_y = state["y"].item()

        # write state name in the map
        name_writer.color("black")
        name_writer.penup()
        name_writer.hideturtle()
        name_writer.goto(state_x, state_y)
        name_writer.write(f"{state_name}", move=True, font=FONT)
        score += 1

# print(state_name)`

turtle.mainloop()
