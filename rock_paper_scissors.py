# Rock paper scissors game
import random

choices = ['rock', 'paper', 'scissors']

print("Welcome to the rock paper scissors game")

while True:
    user_choice = input("Enter your choice: rock, paper or scissors: ").lower()

    if user_choice not in choices:
        print('Invalid choice')
    else:
        computer_choice = random.choice(choices)
        print(f"Computers choice is: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie")
        elif user_choice == 'rock' and computer_choice == 'scissors':
            print("You win")
        elif computer_choice == 'rock' and user_choice == 'scissors':
            print("You lose")
        elif user_choice == 'rock' and computer_choice == 'paper':
            print("You lose")
        elif user_choice == 'paper' and computer_choice == 'rock':
            print("You win")
        elif user_choice == 'paper' and computer_choice == 'scissors':
            print("You lose")
        elif user_choice == 'scissors' and computer_choice == 'paper':
            print("You win")
    

        while True:
            play_again = input("Do you want to play again? Type yes/no: ").lower()
            if play_again == 'yes' or play_again == 'no':
                break
            else:
                print('Invalid input. Please type yes or no.')
        
        if play_again != 'yes':
            print('Hope you had fun playing! Goodbye')
            break