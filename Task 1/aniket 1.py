no_of_games = int(input("enter the number of games you want to play:"))    
def rock_paper_scissor_game(player1_move, player2_move):  
    if player1_move == "rock" and player2_move == "scissor" or player1_move == "scissor" and player2_move == "paper" and player1_move == "paper" and player2_move == "rock":
        return ("player1 wins !!")
    if player2_move == "rock" and player1_move == "scissor" or player2_move == "scissor" and player1_move == "paper" or player2_move == "paper" and player1_move == "rock":
        return ("player2 wins!!!")
    else :
        return ("game got tie , start the game again ")
n=1
while(n<=no_of_games):
    player1_move = input("enter your move player1 :")
    player2_move = input("enter your move player2 :")
    print(rock_paper_scissor_game(player1_move ,player2_move))
    n+=1

     



      


