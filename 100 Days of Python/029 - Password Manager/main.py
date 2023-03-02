from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

DEFAULT_USER = "0xskar@proton.me"
LABEL_FONTS = ("Arial", 9, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))] + [choice(symbols) for _ in range(randint(2, 4))] + [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    username = user_entry.get()
    password = password_entry.get()

    if not website or not username or not password:
        messagebox.showerror(title="Oops", message="You can have any empty fields.")
    else:
        # Check if inputs okay
        is_okay = messagebox.askokcancel(title="Confirm Information",
                                         message=f"Is this information correct?\nWebsite: {website}\nEmail/Username: {username}\nPassword: {password}")
        if is_okay:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

main_canvas_image = PhotoImage(file="logo.png")
main_canvas = Canvas(width=200, height=200, highlightthickness=0)
main_canvas.create_image(100, 100, image=main_canvas_image)
main_canvas.grid(column=1, row=0)

website_entry_label = Label(text="Website:", font=LABEL_FONTS)
website_entry_label.grid(column=0, row=1)
website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

user_entry_label = Label(text="Email/Username:", font=LABEL_FONTS)
user_entry_label.grid(column=0, row=2)
user_entry = Entry(width=52)
user_entry.insert(0, DEFAULT_USER)
user_entry.grid(column=1, row=2, columnspan=2)

password_entry_label = Label(text="Password:", font=LABEL_FONTS)
password_entry_label.grid(column=0, row=3)
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)
password_generate_button = Button(text="Generate Password", font=LABEL_FONTS, command=generate_password)
password_generate_button.grid(column=2, row=3)

add_button = Button(text="Add", font=LABEL_FONTS, width=40, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
