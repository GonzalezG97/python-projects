import random

def play():
    user = input('Rock(R), Paper(P), Scissors(S) ').lower()
    comp = random.choice(['r', 'p', 's'])
    if user == comp:
        return "Its a tie"
    if winCon(user, comp):
        return "Victory for you and your family!"

def winCon(user, comp):
    if (user == 'r' and comp == 's') or (user == 'p' and comp == 'r') or (user == 's' and comp == 'p'):
        return True

play()