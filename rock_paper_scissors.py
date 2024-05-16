import random

def print_instructions():
    print("Welcome to the rock-paper-scissors game!\n")
    print("Instructions:")
    print("Enter 'rock', 'paper', or 'scissors'.")
    print("After each round, you will be asked if you want to play again.")
    print("You can type 'quit' to exit the game at any time.\n")

def get_user_choice():
    return input("Enter your choice: rock, paper, or scissors: ").lower()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return "You win"
    elif computer_choice == 'rock' and user_choice == 'scissors':
        return "You lose"
    elif user_choice == 'rock' and computer_choice == 'paper':
        return "You lose"
    elif user_choice == 'paper' and computer_choice == 'rock':
        return "You win"
    elif user_choice == 'paper' and computer_choice == 'scissors':
        return "You lose"
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return "You win"

def play_again():
    while True:
        play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
        if play_again == 'yes' or play_again == 'no':
            return play_again
        else:
            print('Invalid input. Please type yes or no.')

def main():
    print_instructions()

    while True:
        user_choice = get_user_choice()
        
        if user_choice == 'quit':
            print('\nThank you for playing! Goodbye')
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print('Invalid choice. Please enter rock, paper, or scissors.')
            continue

        computer_choice = get_computer_choice()
        print(f"Computer's choice is: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if play_again() != 'yes':
            print('\nHope you had fun playing! Goodbye\n')
            break

if __name__ == "__main__":
    main()
