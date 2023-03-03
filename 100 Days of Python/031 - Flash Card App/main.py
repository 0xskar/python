from tkinter import *
from flashcards import Flashcard

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
TEXT_FONT = ("Arial", 60, "bold")
flashcard = Flashcard()


def card_picker_right():
    current_word = flashcard_canvas.itemcget(flashcard_text, "text")
    title_1, text_1, title_2, text_2 = flashcard.new_card(0, current_word)
    flashcard_canvas.itemconfig(flashcard_title, text=title_2, fill="black")
    flashcard_canvas.itemconfig(flashcard_text, text=text_2, fill="black")
    flashcard_canvas.itemconfig(canvas_image, image=flashcard_canvas_image_front)
    window.after(3000, flip_card, title_1, text_1)


def card_picker_wrong():
    current_word = flashcard_canvas.itemcget(flashcard_text, "text")
    title_1, text_1, title_2, text_2 = flashcard.new_card(1, current_word)
    flashcard_canvas.itemconfig(flashcard_title, text=title_2, fill="black")
    flashcard_canvas.itemconfig(flashcard_text, text=text_2, fill="black")
    flashcard_canvas.itemconfig(canvas_image, image=flashcard_canvas_image_front)
    window.after(3000, flip_card, title_1, text_1)


def flip_card(title, text):
    flashcard_canvas.itemconfig(flashcard_title, text=title, fill="white")
    flashcard_canvas.itemconfig(flashcard_text, text=text, fill="white")
    flashcard_canvas.itemconfig(canvas_image, image=flashcard_canvas_image_back)


window = Tk()
window.title("Language Learner")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flashcard_canvas_image_front = PhotoImage(file="images/card_front.png")
flashcard_canvas_image_back = PhotoImage(file="images/card_back.png")
flashcard_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = flashcard_canvas.create_image(400, 263, image=flashcard_canvas_image_front)
flashcard_title = flashcard_canvas.create_text(400, 150, text="Get", font=TITLE_FONT)
flashcard_text = flashcard_canvas.create_text(400, 265, text="Ready!", font=TEXT_FONT)
flashcard_canvas.grid(column=0, row=0, columnspan=2)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(command=card_picker_wrong, image=wrong_button_image, highlightthickness=0, borderwidth=0)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(command=card_picker_right, image=right_button_image, highlightthickness=0, borderwidth=0)
right_button.grid(column=1, row=1)

window.mainloop()
