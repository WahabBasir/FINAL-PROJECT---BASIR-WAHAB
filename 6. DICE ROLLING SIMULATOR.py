print('BASIR P. WAHAB')
print('1BSCE-B')
print()
print('ICT 09 Programming 1')
print('FINAL PROJECT')
print()
print('PYTHON PROJECT 6 - DICE ROLLING SIMULATOR')
print()
print()

import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator Game!")
    print("==========================================")
    print("Rules: Each player will roll a dice. The player who wins 2 out of 3 rounds wins the game.")
    print()
    
    player1_wins = 0
    player2_wins = 0
    rounds_to_win = 2
    round_number = 1
    
    while player1_wins < rounds_to_win and player2_wins < rounds_to_win:
        print(f"Round {round_number}:")
        print("-------------")
        
        # Player 1 rolls the dice
        input("Player 1, press Enter to roll the dice...")
        player1_dice = roll_dice()
        print(f"Player 1 rolled: {player1_dice}")
        
        # Player 2 rolls the dice
        input("Player 2, press Enter to roll the dice...")
        player2_dice = roll_dice()
        print(f"Player 2 rolled: {player2_dice}")
        
        # Determine the round winner
        if player1_dice > player2_dice:
            print("Player 1 wins this round!\n")
            player1_wins += 1
        elif player2_dice > player1_dice:
            print("Player 2 wins this round!\n")
            player2_wins += 1
        else:
            print("It's a tie for this round!\n")
        
        round_number += 1
    
    # Determine the overall winner
    if player1_wins > player2_wins:
        print("Player 1 wins the game!")
    else:
        print("Player 2 wins the game!")

if __name__ == "__main__":
    main()
