import turtle
from game_brain import GameBrain

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
bg_img = "blank_states_img.gif"
screen.addshape(bg_img)
turtle.shape(bg_img)
states = GameBrain()

guessing = True
while guessing:
    answer_state = screen.textinput(title=f"{len(states.correct_guesses)}/50 States Correct", prompt="Guess a state name: ").title()
    if answer_state == "Exit":
        break
    states.answer_check(state_guess=answer_state)
    if len(states.correct_guesses) == 50:
        print("you guessed all the states")

states.game_exit_export_states()

screen.exitonclick()
