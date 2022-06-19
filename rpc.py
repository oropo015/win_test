import random

# r < s s < p p < r

def check_rpc():
    trial = 3
    game = ['r', 'p', 's']
    computer_guess = random.choice(game)
    print(f'================YOU HAVE {trial} trials================' )
    player_guess = input('Enter your guess, r for Rock. p for Paper, and s for Scissors:').lower()
    while trial != 0:
        trial = trial - 1
        if player_guess != 's' and player_guess != 'p' and player_guess != 'r' : 
            print(f'invalid guess {player_guess}')
            player_guess = input('Enter your guess, r for Rock. p for Paper, and s for Scissors:').lower()
            if trial == 0:
                print('You exhausted your trials')
                break
                
            elif trial == 1:
                print(f'Remaining {trial} trial')
            else:
                print(f'Remaining {trial} trials')
        else:
            return computer_guess + player_guess

print(check_rpc())


