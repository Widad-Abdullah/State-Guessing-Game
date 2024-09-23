from turtle import Turtle,Screen
import pandas

screen=Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
img=Turtle()
img.shape("blank_states_img.gif")

data=pandas.read_csv("50_states.csv")
states=data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:
    guess = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state name...").title()

    if guess=="Exit":
        not_guessed = [n for n in states if n not in guessed_states]
        pandas.DataFrame(not_guessed).to_csv("states_to_learn.csv")
        break
    elif guess in states:
        guessed_states.append(guess)
        turtle=Turtle()
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(data[data.state==guess].x.item(),data[data.state==guess].y.item())
        turtle.write(guess)


