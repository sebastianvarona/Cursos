#Imports
from random import randint
from time import sleep

def animation(failures):
    while failures<=6:
        if failures==0:
            print("""
                ______
                |    
                |  
                |
                |
            --------
                    """)
        elif failures==1:
            print("""
                ______
                |    O
                |  
                |
                |
            --------
                """)
        elif failures==2:
            print("""
                ______
                |    O
                |    |
                |
                |
            --------
                """)
        elif failures==3:
            print("""
                ______
                |    O
                |   /|
                |
                |
            --------
                """)
        elif failures==4:
            print("""
                ______
                |    O
                |   /|\\
                |
                |
            --------
                """)
        elif failures==5:
            print("""
                ______
                |    O
                |   /|\\
                |   /
                |
            --------
                """)
        else:
            print("""
                ______
                |    O
                |   /|\\
                |   / \\
                |
            --------
            """)
            failures = 0
        break

def principal():
    failures = 0
    player = 1
    dictio = {1:'gravel', 2:'west',3:'teach',4:'predator',5:'legislature',6:'executive',7:'allocation',8:'communication',9:'track',10:'clash',11:'occupation',12:'business',13:'curve'}
    word = dictio[randint(1,13)]
    appeOne = []
    appeTwo = []
    
    for w in word:
        appeOne.append('_')
        appeTwo.append('_')
    while True:
        print(chr(27) + "[2J")
        if player==1:
            print('Player\'s 1 turn')
            animation(failures)
            print('GUESS THE WORD:')
            print(appeOne)
            guess= input('Guess a letter... ').lower()
            if guess in word:
                i = 0
                for w in word:
                    if guess == w:
                        appeOne[i] = guess
                        i+=1
                    else:
                        i+=1
                animation(failures)
                print(appeOne)
            else:
                failures+=1
                animation(failures)
                print(appeOne)
            player = 2

        else:
            print('Player\'s 2 turn')
            animation(failures)
            print('GUESS THE WORD:')
            print(appeTwo)
            guess= input('Guess a letter... ').lower()
            if guess in word:
                i = 0
                for w in word:
                    if guess == w:
                        appeTwo[i] = guess
                        i+=1
                    else:
                        i+=1
                animation(failures)
                print(appeTwo)
            else:
                failures+=1
                animation(failures)
                print(appeTwo)
            player=1

        if failures == 6:
            print('There\'s no winner')
            break
        if '_' not in appeOne:
            print('Player 1 wins')
            break
        if '_' not in appeTwo:
            print('Player 2 wins')
            break
        sleep(2)
        

    
principal()


