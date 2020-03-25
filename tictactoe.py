#------------------TIC-TAC-TOE GAME FOR TWO PLAYERS----------------------------------------
print('------T I C . T A C . T O E-------')

player1=input('\nPlayer 1: Choose o or x : ' )

if player1=='x':
    player2='o'
else:
    player2='x'

print(f'Player 2: {player2}')

#Count Chances
board_list=[1,2,3,4,5,6,7,8,9,10]     

#Initially no input
outcome=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']       

#----------------------------------W I N  F U N C T I O N-------------------------------------------------------

def is_win(player):
    if (set(outcome[7:10]) == set(player) or set(outcome[4:7]) == set(player) or
            set(outcome[1:4]) == set(player)):
        return True
    elif (outcome[8]==outcome[5]==outcome[2] == player) or (outcome[7]==outcome[4]==outcome[1] == player) or (outcome[9]==outcome[6]==outcome[3] == player):
        return True
    elif (outcome[7]==outcome[5]==outcome[3] == player) or (outcome[1]==outcome[5]==outcome[9] == player) :
        return True
    else:
        return False

#-------------------------------------PRINTING BOARD----------------------------------------------------

def display_board(board):
        print('''
                  |      |
               {}  |  {}   |  {}
                  |      |
            """"""""""""""""""""
                  |      |
               {}  |  {}   |  {}
                  |      |
            """""""""""""""""""""
                  |      |
               {}  |  {}   |  {}
                  |      |    
        
        '''.format(board[7],board[8],board[9],board[4],board[5],board[6],board[1],board[2],board[3]))

#-------------------------------------------M A I N------------------------------------------------

play = input('Do you want to start the game(yes/no): ')
while play == 'yes':
    outcome=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    for num in board_list:
        display_board(outcome)
        if num==10:
            print("GAME OVER!\nIt's a TIE!")
            break

        elif is_win(player1):
            print('GAME OVER!\nPlayer 1  WINS!')
            break

        elif is_win(player2):
            print('GAME OVER!\nPlayer 2  WINS!')
            break

        elif num%2!=0:
            digit=int(input('Player 1: \nMake your chance '))
            outcome[digit]=player1
            print('\n'*100)
            display_board((outcome))

        elif num%2==0:
            digit=int(input('Player 2: \nMake your chance '))
            outcome[digit]=player2
            print('\n'*100)
            display_board((outcome))

        else:
            print('Invalid Input')
            break

    play = input('Do you want to PLAY AGAIN(yes/no) : ')

#--------------------------------------------------E N D--------------------------------------------------
