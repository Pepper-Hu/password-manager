import tkinter as tk
from tkinter import PhotoImage
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# window
window = tk.Tk()
window.title("Password Manager")
window.configure(background="white", padx=20, pady=20)

# canvas
canvas = tk.Canvas(bg="white", height=200, width=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()











window.mainloop()