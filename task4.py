import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice):
    global user_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    # Update the labels
    result_label.config(text=f"Result: {result}")
    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    score_label.config(text=f"Score - You: {user_score}, Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Result: ")
    user_choice_label.config(text="Your choice: ")
    computer_choice_label.config(text="Computer's choice: ")
    score_label.config(text="Score - You: 0, Computer: 0")

# Initialize main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Initialize scores
user_score = 0
computer_score = 0

# Widgets for the game
title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Helvetica", 16))
title_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", font=("Helvetica", 14), command=lambda: determine_winner("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Helvetica", 14), command=lambda: determine_winner("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Helvetica", 14), command=lambda: determine_winner("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

user_choice_label = tk.Label(root, text="Your choice: ", font=("Helvetica", 14))
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer's choice: ", font=("Helvetica", 14))
computer_choice_label.pack()

result_label = tk.Label(root, text="Result: ", font=("Helvetica", 14), fg="blue")
result_label.pack()

score_label = tk.Label(root, text="Score - You: 0, Computer: 0", font=("Helvetica", 14), fg="green")
score_label.pack()

reset_button = tk.Button(root, text="Reset Game", font=("Helvetica", 14), command=reset_game)
reset_button.pack(pady=10)

# Run the main loop
root.mainloop()
