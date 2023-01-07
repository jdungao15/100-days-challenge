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
guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{score}/50 Guess the states",
                                    prompt="What's another state's name").title()


    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

        # check answer
    if answer_state in state_list:
        state = state_data[state_data["state"] == answer_state]
        guessed_state.append(answer_state)

        # write state name in the map
        name_writer.color("black")
        name_writer.penup()
        name_writer.hideturtle()
        name_writer.goto(state.x.item(), state.y.item())
        name_writer.write(f"{answer_state}", move=True, font=FONT)
        score += 1
    print(guessed_state)
    print(missing_states)




