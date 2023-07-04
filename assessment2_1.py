"""
Assessment 2.1 - Random Number Guesser

Write a program that asks the user to enter two integers representing the start and end of a range.
The program should then generate a random number within this range (inclusicvely) and ask  the user to guess numbers until
they guess the randomly generated number. Once the user guesses the random number, the program should  tell them how many attempts
it took them to guess it.

Your program needs to ensure that the range of numbers given is valid. For example, if  the user enters a number for the end of the
range that is less than the start of the range your program needs ask them to enter a valid number. Your program must also handle 
any other errors that might occur, like the user entering a string instead of an integer.

Note: You may assume the start of the range will never be negative (i.e. you don't need to handle  negatve values).
"""

import random

start = input("Enter the start of the range: ")
while not start.isdigit():
    print("Please enter a valid number.")
    start = input("Enter the start of the range: ")

end = input("Enter the end of the range: ")
while not end.isdigit() or int(start) > int(end):
    print("Please enter a valid number.")
    end = input("Enter the end of the range: ")

number = random.randint(int(start), int(end))

guess = None
count = 0

while guess != number:
    guess = input("Guess a number: ")
    while not guess.isdigit() or int(guess) > int(end) or int(guess) < int(start):
        print("Please enter a valid number.")
        guess = input("Guess a number: ")
    count += 1
    guess = int(guess)

suffix = ""
if count > 1:
    suffix = "s"

print(f"You guessed the number in {count} attempt{suffix}")
        
        