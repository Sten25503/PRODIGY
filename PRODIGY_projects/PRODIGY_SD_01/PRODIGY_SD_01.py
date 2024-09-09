import tkinter as tk
from tkinter import messagebox

# Function to convert temperatures
def convert_temperature():
    try:
        temp_value = float(temp_entry.get())
        unit = unit_var.get()

        if unit == "C":
            fahrenheit = (temp_value * 9/5) + 32
            kelvin = temp_value + 273.15
            result_label.config(text=f"{temp_value}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K")
        elif unit == "F":
            celsius = (temp_value - 32) * 5/9
            kelvin = celsius + 273.15
            result_label.config(text=f"{temp_value}°F = {celsius:.2f}°C = {kelvin:.2f}K")
        elif unit == "K":
            celsius = temp_value - 273.15
            fahrenheit = (celsius * 9/5) + 32
            result_label.config(text=f"{temp_value}K = {celsius:.2f}°C = {fahrenheit:.2f}°F")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for temperature.")

# Setting up the GUI window
root = tk.Tk()
root.title("Temperature Conversion")

# Temperature Entry
tk.Label(root, text="Enter Temperature:").grid(row=0, column=0)
temp_entry = tk.Entry(root)
temp_entry.grid(row=0, column=1)

# Unit selection
tk.Label(root, text="Select Unit:").grid(row=1, column=0)
unit_var = tk.StringVar(value="C")
tk.Radiobutton(root, text="Celsius (°C)", variable=unit_var, value="C").grid(row=1, column=1)
tk.Radiobutton(root, text="Fahrenheit (°F)", variable=unit_var, value="F").grid(row=1, column=2)
tk.Radiobutton(root, text="Kelvin (K)", variable=unit_var, value="K").grid(row=1, column=3)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=4)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=4)

# Start the GUI loop
root.mainloop()
