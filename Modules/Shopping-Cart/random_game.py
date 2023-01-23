"""
1. generate a number from 1~10
2. get input from user
3. check input is 1~10
4. check if number is right guess, else guess again
"""

import sys
from random import randint

answer = randint(int(sys.argv[1]), int(sys.argv[2]))


while True:
    try:
        guess = int(input("Guess a number between 1 to 10:  "))
        # if int(guess) > 0 and int(guess) < 11:
        if 0 < guess < 11:
            if guess == answer:
                print("Correct.")
                break
        else:
            print("I said 1 to 10!")
    except ValueError:
        print("Please enter a number.")
        break
