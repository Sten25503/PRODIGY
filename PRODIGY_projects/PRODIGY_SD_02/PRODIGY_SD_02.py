import tkinter as tk
from tkinter import messagebox
import random

# Function to start a new game
def start_new_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0 
    result_label.config(text="I have selected a number between 1 and 100.\nCan you guess it?")
    guess_entry.delete(0, tk.END)
# Function to check the user's guess
def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        attempts += 1
        if guess < secret_number:
            result_label.config(text="Too low! Try again.")
        elif guess > secret_number:
            result_label.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations", f"You've guessed the number {secret_number} in {attempts} attempts!")
            start_new_game()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
# Set up the GUI window
root = tk.Tk()
root.title("Guessing Game")
root.geometry("600x450")
root.resizable(False, False) 
# Main frame to hold everything
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)
# Instruction Label
instruction_label = tk.Label(frame, text="Guess the number between 1 and 100!", font=("Arial", 22))
instruction_label.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
# Guess Entry
guess_label = tk.Label(frame, text="Enter your guess:", font=("Arial", 18))
guess_label.grid(row=1, column=0, padx=10, pady=10)
guess_entry = tk.Entry(frame, font=("Arial", 18), width=10)
guess_entry.grid(row=1, column=1, padx=10, pady=10)
# Guess Button
guess_button = tk.Button(frame, text="Guess", command=check_guess, font=("Arial", 16), bg="lightblue", width=10, height=2)
guess_button.grid(row=2, column=0, columnspan=2, pady=20)
# Result Label
result_label = tk.Label(frame, text="", font=("Arial", 18), fg="green", width=40)
result_label.grid(row=3, column=0, columnspan=2, pady=20)
# Start New Game Button
new_game_button = tk.Button(frame, text="New Game", command=start_new_game, font=("Arial", 16), bg="lightgreen", width=12, height=2)
new_game_button.grid(row=4, column=0, columnspan=2, pady=20)
# Start the game for the first time
start_new_game()
# Start the GUI loop
root.mainloop()
