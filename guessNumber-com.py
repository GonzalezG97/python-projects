import random

def number():
        rNumber = random.randint(0, 3)
        guess = int(input("Guess a Number from 0 to 3! "))
        if guess != rNumber :
            print("Sorry Wrong Number")
        elif guess == rNumber :
            print("Nice Job!")

number ()