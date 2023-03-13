from tkinter import *

def calculate():
    new_calculation = float(kms_input.get())
    output["text"] = (new_calculation * 0.62137119)


window = Tk()
window.title("KMs to Miles Converter")
window.minsize(width=300, height=100)

kms_input = Entry()
kms_input.grid(column=2, row=1)
kms_label = Label(text="KMs")
kms_label.grid(column=3, row=1)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=1, row=2)

output = Label(text=0)
output.grid(column=2, row=2)

output_label = Label(text="Miles")
output_label.grid(column=3, row=2)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=2, row=3)

window.mainloop()