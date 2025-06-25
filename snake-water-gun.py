import random

def determine_winner(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (user == 'rock' and computer == 'paper') or \
         (user == 'paper' and computer == 'scissor') or \
         (user == 'scissor' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ['rock', 'paper', 'scissor']
    user = input("Enter your choice (rock, paper, scissor): ").lower()
    
    if user not in choices:
        print("Invalid choice! Please select rock, paper, or scissor.")
        return

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    
    result = determine_winner(user, computer)
    print(result)

# Run the game
play_game()
