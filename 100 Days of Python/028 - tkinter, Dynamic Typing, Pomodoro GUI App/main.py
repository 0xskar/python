from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#228B22"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    tomato_canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    tomato_canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
tomato_canvas.create_image(100, 112, image=tomato_img)
timer_text = tomato_canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
tomato_canvas.grid(column=1, row=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 25, "bold"), command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", font=(FONT_NAME, 25, "bold"), command=reset_timer)
reset_button.grid(column=2, row=3)

checkmarks = Label(text="", font=(FONT_NAME, 25, "bold"), bg=YELLOW, fg=GREEN)
checkmarks.grid(column=1, row=4)

window.mainloop()
