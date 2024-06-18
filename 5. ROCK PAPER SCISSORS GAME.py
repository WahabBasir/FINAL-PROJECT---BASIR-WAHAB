print('BASIR P. WAHAB')
print('1BSCE-B')
print()
print('ICT 09 Programming 1')
print('FINAL PROJECT')
print()
print('PYTHON PROJECT 5 - ROCK PAPER SCISSORS GAME')
print()
print()

import random

def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please enter either 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "user"
    else:
        return "computer"

def rock_paper_scissors_game():
    print("Welcome to Rock, Paper, Scissors Game!")
    print("==================================================")
    print("Rules: User will pick rock, paper, or scissors. Who wins 2 out of 3 rounds wins the game.")
    user_score = 0
    computer_score = 0
    rounds_to_win = 2

    while user_score < rounds_to_win and computer_score < rounds_to_win:
        print(f"\nUser Score: {user_score} | Computer Score: {computer_score}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "user":
            print("You won this round!")
            user_score += 1
        elif winner == "computer":
            print("Computer won this round!")
            computer_score += 1
        else:
            print("It's a draw!")

    if user_score > computer_score:
        print("\nCongratulations! You won the game!")
    else:
        print("\nComputer won the game. Better luck next time!")

if __name__ == "__main__":
    rock_paper_scissors_game()
