""" 
     '' | '' | '' | '' | '' | '' | ''  #0
    ---------------------------------  #1
     '' | '' | '' | '' | '' | '' | ''  #2
    ---------------------------------  #3
     '' | '' | '' | '' | '' | '' | ''  #4
    ---------------------------------  #5
     '' | '' | '' | '' | '' | '' | ''  #6
    ---------------------------------  #7
     '' | '' | '' | '' | '' | '' | ''  #8
    ---------------------------------  #9
     '' | '' | '' | '' | '' | '' | ''  #10
     1    3    5    7    9    11   13
        2    4    6    8    10   12
"""
def draw_field(field):
    for row in range(11):
        if row%2 == 0:
            practicalRow = int(row/2)
            for col in range(13):
                practicalCol = int(col/2)
                if col%2 == 0:
                    if col != 12:
                        print(list_field[practicalRow][practicalCol], end='')
                    else:
                        print(list_field[practicalRow][practicalCol])
                else:
                    print('|', end='')
        else:
            print('-------------')
    print(' ')
    print('1 2 3 4 5 6 7')


list_field = [[' ',' ',' ',' ',' ',' ',' '], #0
              [' ',' ',' ',' ',' ',' ',' '], #1
              [' ',' ',' ',' ',' ',' ',' '], #2
              [' ',' ',' ',' ',' ',' ',' '], #3
              [' ',' ',' ',' ',' ',' ',' '], #4
              [' ',' ',' ',' ',' ',' ',' ']] #5

draw_field(list_field)


#Interactive part with the user
player = 1
game_counter = 0
game_ender = False

while game_ender== False:
    print('Players turn: ', player)
    select_column = int(input('Please select a collumn with the number: '))-1
    if player == 1:
        for position in range(5,-1,-1):
            if list_field[position][select_column] == ' ':
                list_field[position][select_column] = 'X'
                draw_field(list_field)

                #Horizontal check
                for c in range(4):
                    if list_field[position][c]=='X' and list_field[position][c+1]=='X' and list_field[position][c+2]=='X' and list_field[position][c+3]=='X':
                        print('Player 1 wins!!!')
                        game_ender = True
                        break
                for c in range(6,2,-1):
                    if list_field[position][c]=='X' and list_field[position][c-1]=='X' and list_field[position][c-2]=='X' and list_field[position][c-3]=='X':
                        print('Player 1 wins!!!')
                        game_ender = True
                        break
                

                for p in range(5,-1,-1):
                    #Vertical check
                    for c in range(7):
                        if list_field[p][c]=='X' and list_field[p-1][c]=='X' and list_field[p-2][c]=='X' and list_field[p-3][c]=='X':
                            print('Player 1 wins!!!')
                            game_ender = True
                            break
                    #Diagonal check LR        
                    for c in range(4):
                        if list_field[p][c]=='X' and list_field[p-1][c+1]=='X' and list_field[p-2][c+2]=='X' and list_field[p-3][c+3]=='X':
                            print('Player 1 wins!!!')
                            game_ender = True
                            break
                    #Diagonal check RL        
                    for c in range(6,2,-1):
                        if list_field[p][c]=='X' and list_field[p-1][c-1]=='X' and list_field[p-2][c-2]=='X' and list_field[p-3][c-3]=='X':
                            print('Player 1 wins!!!')
                            game_ender = True
                            break


                

                player = 2
                game_counter += 1
                break
    else:
        for position in range(5,-1,-1):
            if list_field[position][select_column] == ' ':
                list_field[position][select_column] = 'O'
                draw_field(list_field)

                #Horizontal check
                for c in range(4):
                    if list_field[position][c]=='O' and list_field[position][c+1]=='O' and list_field[position][c+2]=='O' and list_field[position][c+3]=='O':
                        print('Player 2 wins!!!')
                        game_ender = True
                        break
                for c in range(6,2,-1):
                    if list_field[position][c]=='O' and list_field[position][c-1]=='O' and list_field[position][c-2]=='O' and list_field[position][c-3]=='O':
                        print('Player 2 wins!!!')
                        game_ender = True
                        break
                

                for p in range(5,-1,-1):
                    #Vertical check
                    for c in range(7):
                        if list_field[p][c]=='O' and list_field[p-1][c]=='O' and list_field[p-2][c]=='O' and list_field[p-3][c]=='O':
                            print('Player 2 wins!!!')
                            game_ender = True
                            break
                    #Diagonal check LR        
                    for c in range(4):
                        if list_field[p][c]=='O' and list_field[p-1][c+1]=='O' and list_field[p-2][c+2]=='O' and list_field[p-3][c+3]=='O':
                            print('Player 2 wins!!!')
                            game_ender = True
                            break
                    #Diagonal check RL        
                    for c in range(6,2,-1):
                        if list_field[p][c]=='O' and list_field[p-1][c-1]=='O' and list_field[p-2][c-2]=='O' and list_field[p-3][c-3]=='O':
                            print('Player 2 wins!!!')
                            game_ender = True
                            break

                player = 1
                game_counter += 1
                break


