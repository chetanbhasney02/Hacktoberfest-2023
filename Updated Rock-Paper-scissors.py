import tkinter as tk
import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        return "You win!" if computer_choice == "scissors" else "Computer wins!"
    elif user_choice == "paper":
        return "You win!" if computer_choice == "rock" else "Computer wins!"
    elif user_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "Computer wins!"
    else:
        return "Invalid choice. Please choose rock, paper, or scissors."

def play_game():
    user_choice = user_choice_var.get()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chooses {computer_choice}\n{result}")

# Create a GUI window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")

# Set a fixed GUI size (width x height)
window.geometry("400x400")

# Create a label for the title
title_label = tk.Label(window, text="Rock, Paper, Scissors", font=("Helvetica", 20))
title_label.pack(pady=20)

# Create a label for user instructions
instruction_label = tk.Label(window, text="Choose rock, paper, or scissors:", font=("Helvetica", 12))
instruction_label.pack()

# Create a radio button for user choice
user_choice_var = tk.StringVar()
rock_radio = tk.Radiobutton(window, text="Rock", variable=user_choice_var, value="rock", font=("Helvetica", 12))
paper_radio = tk.Radiobutton(window, text="Paper", variable=user_choice_var, value="paper", font=("Helvetica", 12))
scissors_radio = tk.Radiobutton(window, text="Scissors", variable=user_choice_var, value="scissors", font=("Helvetica", 12))
rock_radio.pack()
paper_radio.pack()
scissors_radio.pack()

# Create a button to play the game
play_button = tk.Button(window, text="Play", command=play_game, font=("Helvetica", 12), bg="green", fg="white")
play_button.pack(pady=20)

# Create a label to display the result
result_label = tk.Label(window, text="", wraplength=250, font=("Helvetica", 14))
result_label.pack()

# Run the GUI application
window.mainloop()
