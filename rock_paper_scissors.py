import random

choices = ['rock', 'paper', 'scissors']

print("Welcome to the rock-paper-scissors game!\n")
print("Instructions:")
print("Enter 'rock', 'paper', or 'scissors'.")
print("After each round, you will be asked if you want to play again.")
print("You can type 'quit' to exit the game at any time.\n")

while True:
    user_choice = input("Enter your choice: rock, paper, or scissors: ").lower()

    if user_choice == 'quit':
        print('\nThank you for playing! Goodbye')
        break

    if user_choice not in choices:
        print('Invalid choice. Please enter rock, paper, or scissors.')
        continue

    computer_choice = random.choice(choices)
    print(f"Computer's choice is: {computer_choice}")

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
        play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
        if play_again == 'yes' or play_again == 'no':
            break
        else:
            print('Invalid input. Please type yes or no.')

    if play_again != 'yes':
        print('\nHope you had fun playing! Goodbye')
        break
