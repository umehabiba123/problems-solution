import random
def user_choice():         # this function take user choice
     while True:
        choice =input("Enter Your Choice scissors, Rock, or Paper ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice: select scissors, Rock, or Paper")

def computer_choice():     # this function take computer choice
     return random.choice(['paper', 'scissors', 'rock'])

def result(user_choice, computer_choice):       # this function show how will win 

    if user_choice == computer_choice:
        print("it's tie")
    elif (user_choice == "rock" and computer_choice == "paper") or (user_choice == "sessior" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("Congrtulation You win !")
    else:
        print("Computer wins !!")
def main():
    while True:
        print("          ******Let's play Rock, Paper, Scissors!******")
        user=user_choice()
        computer=computer_choice()
        print(f"Your choice is {user} and computer choice is {computer}")
        result(user, computer)
        play_again = input("if you want to play again the enter yes : ").lower()
        if play_again != "yes":
            break
    
if __name__ == "__main__":
    main()

