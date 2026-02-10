import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password_on_click():
    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    num_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + num_list

    shuffle(password_list)

    auto_password = "".join(password_list)
    # for char in password_list:
    #   auto_password += char

    print(f"Your password is: {auto_password}")
    password_entry.delete(0, 'end')
    password_entry.insert(0, auto_password)

    # copy the password to clipboard
    pyperclip.copy(auto_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_on_click():
    website = website_entry.get().strip().lower()
    email = email_entry.get().strip()
    password = password_entry.get()
    # get new data from user input
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            # open data.json if it exists
            with open("data.json", "r") as data_file:
                # read old data
                data = json.load(data_file)

        except FileNotFoundError:
            # if data.json does not exist
            print("File not found")
            # create data.json
            with open("data.json", "w") as data_file:
                # write new_data in directly
                json.dump(new_data, data_file, indent=4)

        else:
            # update old data with new data
            data.update(new_data)

            # re-open data.json
            with open("data.json", "w") as data_file:
                # save/write updated data
                json.dump(data, data_file, indent=4)

        finally:
            # reset entry
            website_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

            email_entry.insert(0, "momo@gmail.com")

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_on_click():
    website = website_entry.get().strip().lower()

    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please enter the website!")
    else:
        try:
            # open data.json if it exists
            with open("data.json", "r") as data_file:
                # read data
                data = json.load(data_file)

        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
            # clear only the website field for retry
            website_entry.delete(0, 'end')
            website_entry.focus()

        else:
            try:
                target_data = data[website]
            except KeyError:
                # if data_file exists but data not found
                messagebox.showinfo(title="Error", message=f"No details exists for {website}")
            else:
                # if data_file exists and data found
                messagebox.showinfo(title=f"{website.title()}", message=f"Email: {target_data["email"]}\nPassword: {target_data["password"]}")

                # reset entry only when data found
                website_entry.delete(0, 'end')
                email_entry.delete(0, 'end')
                password_entry.delete(0, 'end')

                email_entry.insert(0, "momo@gmail.com")

# ---------------------------- UI SETUP ------------------------------- #
# window
window = tk.Tk()
window.title("Password Manager")
window.configure(background="white", padx=50, pady=50)

# canvas
canvas = tk.Canvas(bg="white", height=200, width=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# label
website_label = tk.Label(text="Website: ", bg="white", fg="black", pady=5)
website_label.grid(row=1, column=0, sticky='E')

email_label = tk.Label(text="Email/Username: ", bg="white", fg="black",  pady=5)
email_label.grid(row=2, column=0, sticky='E')

password_label = tk.Label(text="Password: ", bg="white", fg="black", pady=5)
password_label.grid(row=3, column=0, sticky='E')

# entry
website_entry = tk.Entry(width=30, highlightthickness=1)
website_entry.grid(row=1, column=1, sticky='W')
website_entry.focus()

email_entry = tk.Entry(width=52, highlightthickness=1)
email_entry.grid(row=2, column=1, columnspan=2, sticky='W')
email_entry.insert(0, "momo@gmail.com")

password_entry = tk.Entry(width=30, highlightthickness=1)
password_entry.grid(row=3, column=1, sticky='W')

# btn
search_btn = tk.Button(text="Search", width=15, command=search_on_click)
search_btn.grid(row=1, column=2, sticky='W')

generate_btn = tk.Button(text="Generate Password", width=15, command=generate_password_on_click)
generate_btn.grid(row=3, column=2, sticky='W')

add_btn = tk.Button(text="Add", width=44, command=add_on_click)
add_btn.grid(row=4, column=1, columnspan=2, sticky='W')


window.mainloop()