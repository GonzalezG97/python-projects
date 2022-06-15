import random

def autoGuess(x,y):
    magicNum = random.randint(x,y)
    guess = random.randint(x, y)
    print(magicNum)
    print(guess)

autoGuess(1,5)