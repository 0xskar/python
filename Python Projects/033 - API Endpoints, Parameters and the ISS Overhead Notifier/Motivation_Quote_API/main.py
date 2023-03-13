from tkinter import *
import requests
import random

response = requests.get(url="https://zenquotes.io/api/quotes")
response.raise_for_status()
data = response.json()


def get_quote():
    random_num = random.randint(0, len(data))
    random_text = data[random_num]['q']
    random_author = data[random_num]['a']
    canvas.itemconfig(quote_text, text=random_text)
    canvas.itemconfig(quote_author, text=random_author)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
quote_author = canvas.create_text(50, 380, text="Author")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()