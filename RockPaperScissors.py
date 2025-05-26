import random
Print("Prajwal BR\nUSN:1AY24AI083\nSEc:O")
def rock_paper_scissors():
    print("Welcome to Rock Paper Scissors!")
    print("Enter your choice: rock, paper, or scissors")
    print("Type 'quit' to exit the game")
    
    choices = ['rock', 'paper', 'scissors']
    score = {'player': 0, 'computer': 0, 'ties': 0}
    
    while True:
        player_choice = input("\nYour choice: ").lower()
        
        if player_choice == 'quit':
            print("\nFinal Score:")
            print(f"Player: {score['player']}  Computer: {score['computer']}  Ties: {score['ties']}")
            print("Thanks for playing!")
            break
            
        if player_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue
            
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if player_choice == computer_choice:
            print("It's a tie!")
            score['ties'] += 1
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            score['player'] += 1
        else:
            print("Computer wins!")
            score['computer'] += 1

rock_paper_scissors()
