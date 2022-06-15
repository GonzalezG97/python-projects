import random 
#The computer will now guess our number
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        compNum = random.randint(low, high)
        feedback = input(f'Is this {compNum} too high (H), too low (L) or correct (C)? ').lower()
        if feedback == 'h':
            high = compNum - 1
        

computer_guess(5)