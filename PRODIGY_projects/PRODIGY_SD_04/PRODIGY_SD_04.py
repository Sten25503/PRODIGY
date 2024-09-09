import tkinter as tk
from tkinter import messagebox
import random

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0 
                return False
    return True

def generate_full_sudoku(board):
    solve_sudoku(board)

def remove_numbers(board, difficulty=30):
    for _ in range(difficulty):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0

# Function to generate a new valid Sudoku puzzle
def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    
    # Generate a fully solved Sudoku board
    generate_full_sudoku(board)
    
    # Make a copy of the solved board
    solution_board = [row[:] for row in board]
    
    # Remove some numbers to create the puzzle
    remove_numbers(board, difficulty=30)
    return board, solution_board

def update_board_display(board, entries):
    for row in range(9):
        for col in range(9):
            entries[row][col].delete(0, tk.END)
            if board[row][col] != 0:
                entries[row][col].insert(tk.END, str(board[row][col]))

# Function to start solving the Sudoku puzzle
def solve_puzzle():
    global solution_board
    if solve_sudoku(solution_board):
        update_board_display(solution_board, entries)
    else:
        messagebox.showerror("Error", "No solution exists for this Sudoku puzzle.")

# Function to reset the grid with a new random puzzle
def reset_grid():
    global current_board, solution_board
    current_board, solution_board = generate_sudoku()
    update_board_display(current_board, entries)

# Main GUI setup
root = tk.Tk()
root.title("Sudoku Solver")
root.geometry("400x450")
frame = tk.Frame(root)
frame.pack(pady=10)

# Create a 9x9 grid
entries = []
for row in range(9):
    current_row = []
    for col in range(9):
        entry = tk.Entry(frame, width=2, font=("Arial", 18), justify="center")
        entry.grid(row=row, column=col, padx=5, pady=5)
        current_row.append(entry)
    entries.append(current_row)

# Buttons to solve the puzzle and reset the grid with a new random puzzle
solve_button = tk.Button(root, text="Solve", command=solve_puzzle, font=("Arial", 14), bg="lightgreen")
solve_button.pack(side=tk.LEFT, padx=20, pady=20)
reset_button = tk.Button(root, text="New Puzzle", command=reset_grid, font=("Arial", 14), bg="lightcoral")
reset_button.pack(side=tk.RIGHT, padx=20, pady=20)

# Initialize the board with a new puzzle
current_board, solution_board = generate_sudoku()
# Start the game with a random puzzle
update_board_display(current_board, entries)
# Start the Tkinter event loop
root.mainloop()
