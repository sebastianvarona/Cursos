def drawField(field):
    for row in range(5):
        if row % 2 == 0:
            practicalRow = int(row/2)
            for col in range(5):
                if col % 2 == 0:
                    practicalCol = int(col/2)
                    if col != 4:
                        print(field[practicalRow][practicalCol], end='')
                    else:
                        print(field[practicalRow][practicalCol])
                else:
                    print('|', end='')
        else:
            print('-----')


player = 1
currentField = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
drawField(currentField)
while True:
    print('Players turn: ', player)
    moveRow = int(input('Digite la hilera 0,1 o 2: \n'))
    moveCol = int(input('Digite la columna 0,1 o 2: \n'))
    if player == 1:
        if currentField[moveRow][moveCol] == ' ':
            currentField[moveRow][moveCol] = 'X'
            player = 2
    else:
        if currentField[moveRow][moveCol] == ' ':
            currentField[moveRow][moveCol] = 'O'
            player = 1
    drawField(currentField)
