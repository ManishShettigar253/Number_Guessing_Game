import tkinter as tk
from tkinter import messagebox
from random import randint

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.add_title()
        self.min_value = 1
        self.max_value = 10
        self.number = randint(self.min_value, self.max_value)
        
        self.setup_range_input()
        self.setup_game()

    def add_title(self):
        self.title_label = tk.Label(self.root, text="Number Guessing Game", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

    def setup_range_input(self):
        # Frame for range inputs
        self.range_frame = tk.Frame(self.root)
        self.range_frame.pack(pady=10)

        # Min value input
        self.min_label = tk.Label(self.range_frame, text="Min:")
        self.min_label.grid(row=0, column=0)
        self.min_entry = tk.Entry(self.range_frame)
        self.min_entry.grid(row=0, column=1)

        # Max value input
        self.max_label = tk.Label(self.range_frame, text="Max:")
        self.max_label.grid(row=0, column=2)
        self.max_entry = tk.Entry(self.range_frame)
        self.max_entry.grid(row=0, column=3)

        self.set_range_button = tk.Button(self.range_frame, text="Set Range", command=self.set_range)
        self.set_range_button.grid(row=0, column=4)

    def setup_game(self):
        # Frame for guessing
        self.guess_frame = tk.Frame(self.root)
        self.guess_frame.pack(pady=10)

        self.guess_label = tk.Label(self.guess_frame, text="Guess a number:")
        self.guess_label.pack(side=tk.LEFT)
        
        self.guess_entry = tk.Entry(self.guess_frame)
        self.guess_entry.pack(side=tk.LEFT)
        
        self.guess_button = tk.Button(self.guess_frame, text="Guess", command=self.check_guess)
        self.guess_button.pack(side=tk.LEFT)
        
    def set_range(self):
        try:
            self.min_value = int(self.min_entry.get())
            self.max_value = int(self.max_entry.get())
            if self.min_value >= self.max_value:
                raise ValueError("Minimum value must be less than maximum value.")
            self.number = randint(self.min_value, self.max_value)
            messagebox.showinfo("Range Set", f"Range is set from {self.min_value} to {self.max_value}. Start guessing!")
        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid input: {ve}")

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            if guess < self.min_value or guess > self.max_value:
                raise ValueError(f"Guess must be between {self.min_value} and {self.max_value}.")
            if guess == self.number:
                messagebox.showinfo("Result", "You guessed it right!")
            else:
                messagebox.showinfo("Result", f"Sorry, your guess was wrong. The correct number is {self.number}")
            self.number = randint(self.min_value, self.max_value)  # Reset the number for a new game
        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid input: {ve}")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
