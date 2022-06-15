import random
#User creates range and comp guess random number chosen by the computer
def autoGuess():
    firstNum = int(input('What should be the lower number be? '))
    secNum = int(input('What should the highest number be? '))
    magicNum = random.randint(firstNum,secNum)
    guess = random.randint(firstNum,secNum)
    while guess != magicNum:
        guess = random.randint(firstNum,secNum)
        print('Missed the mark, keep trying')
    print(f'Nice job! The number was {magicNum}')

autoGuess()