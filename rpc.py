import random

def play():
    user = input('Rock(R), Paper(P), Scissors(S) ').lower()
    comp = random.choice(['r', 'p', 's'])
    if user == comp:
        print("Its a tie")
    if winCon(user, comp):
        print("Victory for you and your family!")
    
    print('Better luck next time!')

def winCon(player, computer):
    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        return True

play()