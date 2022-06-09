import random

def number(x):
        rNumber = random.randint(0, 3)
        guess = x
        if guess != rNumber :
            print("Sorry Wrong Number")
        elif guess == rNumber :
            print("Nice Job!")

number (2)