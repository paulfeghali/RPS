import random

def play():
    user = input('Select rock (R), paper (P), or scissors(S)').lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer: 
        print("It\'s a tie!")

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'

        
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True 

print(play())