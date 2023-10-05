import random

def user_choice():
    user = input("Please Enter Rock, Paper or Scissors:").strip().lower()
    while user not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose Rock, Paper or Scissor")
        user = input("Choose Rock, Paper or Scissors:").strip().lower()
    return user

def computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif(user == "rock" and computer == "scissors" or
    user == "paper" and computer == "rock" or
    user == "scissors" and computer == "paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

def play():
    user = user_choice()
    computer = computer_choice()
    print(f'You choose {user}')
    print(f'Computer chooses {computer}')
    result = winner(user, computer)
    print(result)

while True:
    play()
    play_again = input("Play again? (Yes/No):").strip().lower()
    if play_again != "yes":
        break

print("Game Ends")