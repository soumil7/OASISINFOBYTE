import tkinter as tk
import random
import string
from tkinter import messagebox

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=50, pady=50)
        self.length_entry = tk.Entry(root)
        self.length_entry.grid(row=0, column=1, padx=50, pady=50)

        self.lower_var = tk.IntVar()
        self.lower_check = tk.Checkbutton(root, text="Include Lowercase", variable=self.lower_var)
        self.lower_check.grid(row=1, column=0, columnspan=5, pady=10)

        self.upper_var = tk.IntVar()
        self.upper_check = tk.Checkbutton(root, text="Include Uppercase", variable=self.upper_var)
        self.upper_check.grid(row=2, column=0, columnspan=5, pady=10)

        self.digit_var = tk.IntVar()
        self.digit_check = tk.Checkbutton(root, text="Include Numbers", variable=self.digit_var)
        self.digit_check.grid(row=3, column=0, columnspan=5, pady=10)

        self.symbol_var = tk.IntVar()
        self.symbol_check = tk.Checkbutton(root, text="Include Symbols", variable=self.symbol_var)
        self.symbol_check.grid(row=4, column=0, columnspan=5, pady=10)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, columnspan=5, pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=6, column=0, columnspan=5, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                messagebox.showerror("Error", "Password length must be a positive integer.")
                return

            character_set = ""
            if self.lower_var.get():
                character_set += string.ascii_lowercase
            if self.upper_var.get():
                character_set += string.ascii_uppercase
            if self.digit_var.get():
                character_set += string.digits
            if self.symbol_var.get():
                character_set += string.punctuation

            if not character_set:
                messagebox.showerror("Error", "Select at least one character set.")
                return

            password = ''.join(random.choice(character_set) for _ in range(length))
            self.result_label.config(text=f"Generated Password: {password}")

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
