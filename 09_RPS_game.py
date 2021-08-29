p1 = input("player1 enter your play(R/P/S)): ")

p2 = input("player2 enter your play(R/P/S): ")

rematch = True

while (rematch != False):
   
    if(p1==p2):
        print("its a tie")
    elif(((p1=='R')&(p2=='S'))|((p1=='S')&(p2=='P'))|((p1=='P')&(p2=='R'))):
        print('P1 wins')
    else:
        print('P2 wins')

    rematch = bool(input('want to play again..(True/False)'))


