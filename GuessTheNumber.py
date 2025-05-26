import random
print("Prajwal BR \nUSN:1AY24AI083 \nSec:O")
def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            # Get player's guess
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                return
        
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Game over! The number was {secret_number}.")

guess_the_number()
