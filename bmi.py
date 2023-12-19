import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        self.weight_label = tk.Label(root, text="Weight (kg):")
        self.weight_label.grid(row=0, column=0, padx=10, pady=10)
        self.weight_entry = tk.Entry(root)
        self.weight_entry.grid(row=0, column=1, padx=10, pady=10)

        self.height_label = tk.Label(root, text="Height (m):")
        self.height_label.grid(row=1, column=0, padx=10, pady=10)
        self.height_entry = tk.Entry(root)
        self.height_entry.grid(row=1, column=1, padx=10, pady=10)

        self.calculate_button = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            
            if weight <= 0 or height <= 0:
                messagebox.showerror("Error", "Weight and height must be positive values.")
                return

            bmi = weight / (height ** 2)
            category = self.get_bmi_category(bmi)

            result_text = f"BMI: {bmi:.2f}\nCategory: {category}"
            self.result_label.config(text=result_text)

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values for weight and height.")

    @staticmethod
    def get_bmi_category(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi and bmi < 24.9:
            return "Normal Weight"
        elif 25 <= bmi and bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
