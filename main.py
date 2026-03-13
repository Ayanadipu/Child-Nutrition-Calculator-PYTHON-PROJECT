import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class ChildNutritionCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Child Nutrition Calculator")
        self.root.geometry("400x550")
        self.root.resizable(False, False)

        # Calories per 100g
        self.food_calories = {
            "Milk": 100,
            "Egg": 155,
            "Rice": 130,
            "Lentils": 113,
            "Vegetable": 85,
            "Meat": 143
        }

        # Minimum calorie requirement by age
        self.calorie_requirements = {
            (0, 2): 800,
            (3, 5): 1400,
            (6, 12): 1800
        }

        self.food_intake_entries = {}

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(self.root, text="Child Nutrition Calculator",
                         font=("Arial", 16, "bold"))
        title.pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        # Child details
        tk.Label(frame, text="Child Name").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(frame, text="Age (years)").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(frame)
        self.age_entry.grid(row=1, column=1)

        tk.Label(frame, text="Gender").grid(row=2, column=0, padx=5, pady=5)
        self.gender_var = tk.StringVar()
        gender_box = ttk.Combobox(frame, textvariable=self.gender_var,
                                  values=["Male", "Female"], state="readonly")
        gender_box.grid(row=2, column=1)

        tk.Label(frame, text="Height (cm)").grid(row=3, column=0, padx=5, pady=5)
        self.height_entry = tk.Entry(frame)
        self.height_entry.grid(row=3, column=1)

        tk.Label(frame, text="Weight (kg)").grid(row=4, column=0, padx=5, pady=5)
        self.weight_entry = tk.Entry(frame)
        self.weight_entry.grid(row=4, column=1)

        # Food intake section
        tk.Label(self.root, text="Food Intake (grams)",
                 font=("Arial", 12, "bold")).pack(pady=10)

        food_frame = tk.Frame(self.root)
        food_frame.pack()

        row_index = 0
        for food in self.food_calories:
            tk.Label(food_frame, text=food).grid(row=row_index, column=0, padx=5, pady=3)
            entry = tk.Entry(food_frame)
            entry.grid(row=row_index, column=1)
            self.food_intake_entries[food] = entry
            row_index += 1

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Calculate", command=self.calculate, width=10)\
            .grid(row=0, column=0, padx=10)

        tk.Button(button_frame, text="Clear", command=self.clear_fields, width=10)\
            .grid(row=0, column=1, padx=10)

        tk.Button(button_frame, text="Quit", command=self.root.quit, width=10)\
            .grid(row=0, column=2, padx=10)

    def calculate_bmi(self):
        height_cm = float(self.height_entry.get())
        weight_kg = float(self.weight_entry.get())

        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)

        return bmi

    def get_min_calorie_requirement(self):
        age = int(self.age_entry.get())

        for age_range, calories in self.calorie_requirements.items():
            min_age, max_age = age_range
            if min_age <= age <= max_age:
                return calories

        return 2000  # default if age outside range

    def calculate_daily_calorie_consumption(self):
        total_calories = 0

        for food, entry in self.food_intake_entries.items():

            quantity = entry.get()

            if quantity == "":
                quantity = 0
            else:
                quantity = float(quantity)

            calorie_per_100g = self.food_calories[food]

            total_calories += (calorie_per_100g / 100) * quantity

        return total_calories

    def display_results(self, bmi, min_calories, daily_calories):

        result = f"BMI: {bmi:.2f}\n"
        result += f"Minimum Daily Calories Needed: {min_calories}\n"
        result += f"Calories Consumed: {daily_calories:.2f}\n\n"

        if daily_calories < min_calories:
            result += "⚠ The child may be undernourished."
        else:
            result += "✅ The child's calorie intake is adequate."

        messagebox.showinfo("Nutrition Result", result)

    def clear_fields(self):

        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)

        self.gender_var.set("")

        for entry in self.food_intake_entries.values():
            entry.delete(0, tk.END)

    def validate_inputs(self):

        if not self.name_entry.get():
            messagebox.showwarning("Input Error", "Please enter child's name.")
            return False

        if not self.age_entry.get().isdigit():
            messagebox.showwarning("Input Error", "Please enter a valid age.")
            return False

        if not self.height_entry.get() or not self.weight_entry.get():
            messagebox.showwarning("Input Error", "Enter height and weight.")
            return False

        return True

    def calculate(self):

        try:

            if not self.validate_inputs():
                return

            bmi = self.calculate_bmi()

            min_calories = self.get_min_calorie_requirement()

            daily_calories = self.calculate_daily_calorie_consumption()

            self.display_results(bmi, min_calories, daily_calories)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ChildNutritionCalculatorGUI(root)
    root.mainloop()
