import turtle
import pandas
from turtle import Screen
import csv

turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()
screen = Screen()
screen.title("U.S States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
screen.bgpic("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")

remaining = True
answer_state = screen.textinput(title=f"Guess the State", prompt="What's another state's name?")
guesses = []
states_to_learn = []
score = 0

while len(guesses) < 50:
    states = data["state"].tolist()

    if answer_state in states:
        x = int(data[data.state == answer_state].x)
        y = int(data[data.state == answer_state].y)
        turtle.goto(x, y)
        turtle.write(answer_state)
        score += 1
        guesses.append(answer_state)

    if answer_state == "Exit":
        for state in states:
            if state not in guesses:
                states_to_learn.append(state)
        break
    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name?")

data = pandas.DataFrame(states_to_learn)
data.to_csv("states_to_learn.csv")

print(states_to_learn)
screen.exitonclick()
