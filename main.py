import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password_on_click():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_on_click():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok_save = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail/Username: {email}\nPassword: {password}\nIs it ok to save? ")

        if is_ok_save:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")

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
website_entry = tk.Entry(width=52, highlightthickness=1)
website_entry.grid(row=1, column=1, columnspan=2, sticky='W')
website_entry.focus()

email_entry = tk.Entry(width=52, highlightthickness=1)
email_entry.grid(row=2, column=1, columnspan=2, sticky='W')
email_entry.insert(0, "momo@gmail.com")

password_entry = tk.Entry(width=30, highlightthickness=1)
password_entry.grid(row=3, column=1, sticky='W')

# btn
generate_btn = tk.Button(text="Generate Password", width=15, command=generate_password_on_click)
generate_btn.grid(row=3, column=2, sticky='W')

add_btn = tk.Button(text="Add", width=44, command=add_on_click)
add_btn.grid(row=4, column=1, columnspan=2, sticky='W')


window.mainloop()