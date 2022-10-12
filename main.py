import turtle
import pandas

FONT = ("Arial", 10, "normal")
ALIGNMENT = "center"
guessed_states = []

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Guess the name of a state").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.ht()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, align=ALIGNMENT, font=FONT)
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
