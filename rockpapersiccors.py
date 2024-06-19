def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "It's a tie!"
    elif (choice1 == "rock" and choice2 == "scissors") or \
         (choice1 == "scissors" and choice2 == "paper") or \
         (choice1 == "paper" and choice2 == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Winning rules are as follows:")
    print("Rock vs Paper -> Paper wins")
    print("Rock vs Scissors -> Rock wins")
    print("Paper vs Scissors -> Scissors wins")
    
    player1_choice = input("Player 1, enter your choice (rock, paper, scissors): ").lower()
    player2_choice = input("Player 2, enter your choice (rock, paper, scissors): ").lower()
    
    if player1_choice not in ["rock", "paper", "scissors"] or player2_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
        return
    
    result = determine_winner(player1_choice, player2_choice)
    print(result)
rock_paper_scissors()
