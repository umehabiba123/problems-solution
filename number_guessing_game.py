import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 10)
    
    print("Welcome to the Number Guessing Game!")
    print("I've chosen a number between 1 and 100. Can you guess it?")
    
    while True:
        guess = int(input("Enter your guess: "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            break

# Call the function to start the game
number_guessing_game()