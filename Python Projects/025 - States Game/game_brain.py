from turtle import Turtle
import pandas

STATE_ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")


class GameBrain(Turtle):
    def __init__(self):
        super().__init__()
        self.state_df = pandas.read_csv("50_states.csv")
        self.correct_guesses = []

    def answer_check(self, state_guess):
        state_data = self.state_df[self.state_df['state'] == state_guess]
        if not state_data.empty:
            x, y = state_data.iloc[0]['x'], state_data.iloc[0]['y']
            if state_guess in self.correct_guesses:
                print("Already Guessed.")
                return
            self.update_states(state_guess, x, y)
            self.correct_guesses.append(state_guess)
        else:
            print(f"{state_guess} is not a state.")

    def update_states(self, state_guess, x, y):
        self.color("black")
        self.penup()
        self.hideturtle()
        self.setheading(360)
        self.goto(x=x, y=y)
        self.write(f"{state_guess}", align=STATE_ALIGNMENT, font=FONT)

    def game_exit_export_states(self):
        not_guessed = set(self.state_df['state']) - set(self.correct_guesses)
        with open("./missed_states.txt", mode="w") as states:
            for state in not_guessed:
                states.write(f"\n{state}")



