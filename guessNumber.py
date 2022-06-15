import random
#We are going to try to guess the computers number
def number(x):
        rNumber = random.randint(1, x)
        guess = 0
        while guess != rNumber :
            guess = int(input(f"Guess a Number from 1 to {x}! "))
            if guess == rNumber :
                x = input(print("Nice Job! Do you want to play again?"))
                if x == 'y':
                    number(5)
                    continue
                elif x == 'n':
                    break
                else: 
                    print("Y or N?")
        print("Good bye!")

number (3)