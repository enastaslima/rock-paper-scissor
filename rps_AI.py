from random import randint
player = input("Player's move: ")
rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissor"
print(f"Computer's move: {computer}")

if player == computer: 
    print('Its a tie')
elif player == 'rock':
    if computer == 'scissor':
        print('Player wins')
    elif computer == 'paper':
        print('computer wins')
elif player == 'paper':
    if computer == 'rock':
        print('Player wins')
    elif computer == 'scissor':
        print('computer wins')
elif player == 'scissor': 
    if computer == 'paper':
        print('Player wins')
    elif computer == 'rock':
        print('computer wins')


else:
    print('Something went wrong')
          