from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

DEFAULT_USER = "yaibet@proton.me"
LABEL_FONTS = ("Arial", 9, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def find_password():
    search = website_entry.get().title()
    try:
        with open("data.json", mode="r") as data_file:
            password_data = json.load(data_file)
        if password_data[search]:
            website = search
            password = password_data[search]["password"]
            pyperclip.copy(password)
            messagebox.showinfo(title="Password Exists", message=f"Website: {website}\nPassword: {password}")
    except KeyError:
        messagebox.showerror(title=f"No Password", message=f"No password for {search}")
    except FileNotFoundError:
        messagebox.showerror(title="Datafile Not Found!", message=f"Can't find data. Continue to create new "
                                                                  f"password to create.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

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

    new_data = {
        website.title(): {
            "email": username,
            "password": password,
        }
    }

    if not website or not username or not password:
        messagebox.showerror(title="Oops", message="You can have any empty fields.")
    else:
        try:
            # If file exists, load the data and update
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:  # Create new file if it doesn't exist
            data = new_data

        # Write the updated/new data to the file
        with open("data.json", mode="w") as data_file:
            json.dump(data, data_file, indent=4)

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
website_entry = Entry(width=30)
website_entry.focus()
website_entry.grid(column=1, row=1)
website_search_button = Button(text="Search", font=LABEL_FONTS, command=find_password, width=17)
website_search_button.grid(column=2, row=1)

user_entry_label = Label(text="Email/Username:", font=LABEL_FONTS)
user_entry_label.grid(column=0, row=2)
user_entry = Entry(width=52)
user_entry.insert(0, DEFAULT_USER)
user_entry.grid(column=1, row=2, columnspan=2)

password_entry_label = Label(text="Password:", font=LABEL_FONTS)
password_entry_label.grid(column=0, row=3)
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)
password_generate_button = Button(text="Generate Password", font=LABEL_FONTS, command=generate_password, width=17)
password_generate_button.grid(column=2, row=3)

add_button = Button(text="Add", font=LABEL_FONTS, width=44, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
