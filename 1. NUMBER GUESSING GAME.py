print('BASIR P. WAHAB')
print('1BSCE-B')
print()
print('ICT 09 Programming 1')
print('FINAL PROJECT')
print()
print('PYTHON PROJECT 1 - NUMBER GUESSING GAME')
print()
print()

import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("====================================")
    print("Think of a number between 1 and 100")
    secret_number = random.randint(1, 100)
    
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100")
                continue
            
            if guess == secret_number:
                print(f"Congratulations! You've guessed the correct number in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("Too low! Try guessing a higher number.")
            else:
                print("Too high! Try guessing a lower number.")
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

if __name__ == "__main__":
    number_guessing_game()
