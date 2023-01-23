"""
1. generate a number from 1~10
2. get input from user
3. check input is 1~10
4. check if number is right guess, else guess again
"""

import sys
from random import randint


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("Correct.")
            return True
    else:
        print("I said 1 to 10!")
        return False


if __name__ == "__main__":
    answer = randint(1, 10)

    while True:
        try:
            guess = int(input("Guess a number between 1 to 10:  "))
            if run_guess(guess, answer):
                break
        except ValueError:
            print("Please enter a number.")
            break
