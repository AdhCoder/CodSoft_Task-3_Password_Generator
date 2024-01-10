import secrets
import string
import tkinter as tk
from tkinter import Label, Entry, Button, StringVar

def generate_password(length, custom_symbols):
    adjectives = ["Happy", "Sunny", "Clever", "Gentle", "Brave", "Creative", "Lively", "Charming", "Fierce", "Genuine"]
    nouns = ["Dragon", "Phoenix", "Star", "Wave", "Forest", "Harmony", "Puzzle", "Cascade", "Serenity", "Horizon"]

   
    password_words = [secrets.choice(adjectives), secrets.choice(nouns)]
    remaining_chars = length - sum(map(len, password_words))

 
    symbols = custom_symbols
    password = ''.join(password_words) + ''.join(secrets.choice(string.ascii_letters + string.digits + symbols) for _ in range(remaining_chars))


    password = password[:length]

    return password

def generate_and_display_password():
    length = int(length_var.get())
    custom_symbols = "!@#$%^&*()_-+=<>?/" 
    password = generate_password(length, custom_symbols)
    result_var.set("Generated Password: " + password)


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")


title_label = Label(root, text="Password Generator", font=("Arial", 16, 'italic'), fg="blue")
title_label.pack(pady=10)

length_label = Label(root, text="Enter Password Length:", font=("Arial", 11))
length_label.pack(pady=5)

length_var = StringVar()
length_entry = Entry(root, textvariable=length_var)
length_entry.pack(pady=5)

generate_button = Button(root, text="Generate Password", command=generate_and_display_password, bg="green", fg="white")
generate_button.pack(pady=10)

result_var = StringVar()
result_label = Label(root, textvariable=result_var, font=("Helvetica", 12), wraplength=300, fg="indigo")
result_label.pack(pady=20)


root.mainloop()