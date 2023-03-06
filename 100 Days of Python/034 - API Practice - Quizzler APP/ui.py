from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
UI_FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = quiz_brain.score
        self.window = Tk()
        self.window.title("Quizzle")
        self.window.config(padx=20, bg=THEME_COLOR)

        self.score_text = Label(text=f"Score: {self.score}", font=UI_FONT, fg="white", bg=THEME_COLOR)
        self.score_text.grid(column=1, row=0, pady=20)

        self.main_canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.main_canvas.create_text(150, 125,
            text="",
            font=UI_FONT, width=300)
        self.main_canvas.grid(column=0, row=1, columnspan=2)

        self.true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(command=self.true_response, image=self.true_button_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2, pady=20)

        self.false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(command=self.false_response, image=self.false_button_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        print(self.quiz.still_has_questions())
        self.window.mainloop()

    def get_next_question(self):
        self.main_canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.main_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score_text.config(text=f"Score: {self.quiz.score}")
            self.main_canvas.itemconfig(self.question_text, text="No more questions...")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_response(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_response(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.main_canvas.configure(bg="green")
        else:
            self.main_canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)

