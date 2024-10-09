print("Rock")
print("Paper")
print("Scissors")

player1 = input('Player_1,make your move')
player2 = input('Player_2,make your move')

if player1 == player2: 
    print('Its a tie')
elif player1 == 'rock':
    if player2 == 'scissor':
        print('Player_1 wins')
    elif player2 == 'paper':
        print('Player_2 wins')
elif player1 == 'paper':
    if player2 == 'rock':
        print('Player_1 wins')
    elif player2 == 'scissor':
        print('player_2 wins')
elif player1 == 'scissor': 
    if player2 == 'paper':
        print('Player_1 wins')
    elif player2 == 'rock':
        print('player_2 wins')


else:
    print('Something went wrong')
          

