import tkinter
from playground import add

window = tkinter.Tk()
window.title("My GUI Program")
window.minsize(width=500, height=300)


def button_clicked():
    new_text = text_input.get()
    my_label["text"] = new_text


# label
my_label = tkinter.Label(text="I AM A Label", font=("Arial", 18, "bold"))
my_label["text"] = "I really am a label"
my_label.config(text="label")
my_label.grid(column=1, row=1)

# entry
text_input = tkinter.Entry()
text_input.grid(column=1, row=2)

# button
button = tkinter.Button(text="Button click me", command=button_clicked)
button.grid(column=2, row=3)

window.mainloop()
