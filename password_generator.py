#Program to generate a random password with variable length of letters, numbers and symbols

import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?']

print("Welcome to password generator!")


n_letters = int(input("How many letters do you want in your password? "))
n_numbers = int(input("How many numbers do you want in your password? "))
n_symbols = int(input("How many symbols do you want in your password? "))


passwordL = []

for i in range(1, n_letters + 1 ):
    letter = random.choice(letters)
    passwordL += letter

for i in range(1, n_numbers + 1):
    number = random.choice(numbers)
    passwordL += number

for i in range(1, n_symbols + 1):
    symbol = random.choice(symbols)
    passwordL += symbol

random.shuffle(passwordL)

password = ""

for i in passwordL:
    password += i


print(password)