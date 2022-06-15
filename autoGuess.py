import random

def autoGuess(x,y):
    magicNum = random.randint(x,y)
    guess = random.randint(x, y)
    while guess != magicNum :
        guess = random.randint(x, y)
        print('Not there yet!')
    print('The computer figured it out')
    

autoGuess(1,5)