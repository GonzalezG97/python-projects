import random

def play():
    user = input('Rock(R), Paper(P), Scissors(S)').lower()
    comp = random.choice(['r', 'p', 's'])
    