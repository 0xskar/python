from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


def get_high_score():
    with open("high_scores.txt", mode="r") as file:
        old_high_score = file.read()
    return old_high_score


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(get_high_score())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {get_high_score()}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("high_scores.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
