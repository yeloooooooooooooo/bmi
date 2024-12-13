import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        age = int(age_entry.get())
        gender = gender_var.get()

        height_meters = height / 100

        bmi = weight / (height_meters ** 2)

        normal_range = (18.5, 24.9)

        if normal_range[0] <= bmi <= normal_range[1]:
            health_status = "You're healthy"
        else:
            health_status = "You're unhealthy"

        result_label.config(text=f"Your BMI is: {bmi:.2f}\n{health_status}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for height, weight, and age.")

window = tk.Tk()
window.title("BMI Calculator")

window.geometry("400x300")
window.resizable(False, False)
window.configure(bg="#def5ff")

font_style = ("Poppins", 12)

entry_style = ttk.Style()
entry_style.configure("TEntry",
                      fieldbackground="RED",
                      bordercolor="#def5ff",
                      borderwidth=5,
                      relief="flat",
                      font=font_style)

title_label = tk.Label(window, text="BMI CALCULATOR", font=("Poppins", 16, "bold"), bg="#def5ff")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

age_label = tk.Label(window, text="Age:", font=font_style, bg="#def5ff")
age_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
age_entry = ttk.Entry(window, font=font_style)
age_entry.grid(row=1, column=1, padx=10, pady=5)

height_label = tk.Label(window, text="Height (cm):", font=font_style, bg="#def5ff")
height_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
height_entry = ttk.Entry(window, font=font_style)
height_entry.grid(row=2, column=1, padx=10, pady=5)

weight_label = tk.Label(window, text="Weight (kg):", font=font_style, bg="#def5ff")
weight_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
weight_entry = ttk.Entry(window, font=font_style)
weight_entry.grid(row=3, column=1, padx=10, pady=5)

gender_label = tk.Label(window, text="Gender:", font=font_style, bg="#def5ff")
gender_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")

gender_var = tk.StringVar()
gender_var.set("Male")

male_radiobutton = tk.Radiobutton(window, text="Male", variable=gender_var, value="Male", font=font_style, bg="#def5ff")
male_radiobutton.grid(row=4, column=1, padx=10, pady=5, sticky="w")

female_radiobutton = tk.Radiobutton(window, text="Female", variable=gender_var, value="Female", font=font_style, bg="#def5ff")
female_radiobutton.grid(row=4, column=1, padx=10, pady=5, sticky="e")

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi, font=font_style, cursor="hand2")
calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="", font=font_style, bg="#def5ff")
result_label.grid(row=6, column=0, columnspan=2)

window.mainloop()