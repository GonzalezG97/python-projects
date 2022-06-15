import random 
#The computer will now guess our number
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        ourNum = random.randint(low, high)