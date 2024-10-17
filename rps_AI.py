from random import randint
player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print(f"PLayer Score: {player_wins} Computer Score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissor...")

    player = input("Player's move: ")
    if player =="quit" or player == "q":
         break
    rand_num = randint(0, 2)

    if (rand_num == 0):
        computer = "rock"
    elif (rand_num == 1):
        computer = "paper"
    else:
        computer = "scissor"

    print(f"Computer's move: {computer}")

    if player == computer:
        print("Its a tie")
    elif player == "rock":
        if computer == "paper":
            print("Computer wins")
            computer_wins += 1
        else:
             print("Player wins")
             player_wins += 1
                 
    elif player == "paper":
            if computer == "rock":
                print('player wins')
                player_wins += 1
            else:
                 print("Computer wins")
                 computer_wins += 1
    
    elif player == "scissor":
            if computer == "rock":
                 print("Computer wins")
                 computer_wins += 1
            else:
                 print("You win!")
                 player_wins += 1
    else:
         print("Enter a valid move")       



if player_wins > computer_wins:
     print("Congrats,You won!")
elif player_wins == computer_wins:
     print("It's a tie")
else:
     print("The computer won")
