from random import shuffle, randint
from time import sleep

def create_deck():
    deck = []
    face_values = ['A', 'J', 'Q', 'K']
    suits = {1: 'H', 2: 'S', 3: 'D', 4: 'C'}
    for i in range(1, len(suits)+1):
        for card in range(2, 11):
            ap = str(card) + suits[i]
            deck.append(ap)
        for card in face_values:
            ap = card + suits[i]
            deck.append(ap)
    shuffle(deck)
    return deck

class Player:
    def __init__(self,p):
        self.name = p
        self.hand = self.create_hand()

    def create_hand(self):
        player_hand = []
        for i in range(5):
            player_hand.append(deck[i])
            deck.pop(i)
        return player_hand

    def calc_score(self, card):
        score = 0
        card_value = card[:-1]
        card_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        score += card_dict[card_value]
        return score

    def take(self):
        self.hand.append(deck[0])
        deck.pop(0)

    def put(self, card):
        cards_pile.append(card)
        self.hand.remove(card)

    def game_end(self):
        for card in self.hand:
            cards_pile.append(card)
            self.hand.remove(card)

    def __str__(self):
        currentHand = ''
        for card in self.hand:
            currentHand += card + ' '
        if self.hand != []:
            message = 'Your current hand is: ' + currentHand
        else:
            message = self.name + ' you win!'
        return message

deck = create_deck()
cards_pile = []
last_card = deck.pop(randint(1, 52))
p1 = input('Type your name: ')
p2 = input('Type your name: ')
player1 = Player(p1)
player2 = Player(p2)
player = randint(1, 2)
win = False
moves = 0
message = 'na'
while True:
    if player == 1:
        if player1.hand == []:
            print('{} you are the winner!'.format(p1))
            break
        else:
            pass
    else:
        if player2.hand == []:
            print('{} you are the winner!'.format(p2))
            break
        else:
            pass
        
    print(chr(27) + "[2J")
    print(last_card)
    if player == 1:
        print('{} it\'s your turn'.format(p1))
        print(player1)
    else:
        print('{} it\'s your turn'.format(p2))
        print(player2 )
    action = input('''What are you going to do? (select a number)
    1. Put a card
    2. Take a card from deck
    --> ''')
    if action == '1':
        print(chr(27) + "[2J")
        print(last_card)
        print('What card are you going to use? ')
        if player == 1:
            print(player1)
        else:
            print(player2)
        card = input().upper()
        if last_card == '':
            if player == 1:
                try:
                    player1.put(card)
                    player1_score = player1.calc_score(card)
                    player = 2
                except:
                    print(chr(27) + "[2J")
                    print('The card chosen is not in the deck. If you don\'t have a card of that suit type 2')
                    sleep(3)
                    continue
            else:
                try:
                    player2.put(card)
                    player2_score = player2.calc_score(card)
                    player = 1
                except:
                    print(chr(27) + "[2J")
                    print('The card chosen is not in the deck. If you don\'t have a card of that suit type 2')
                    sleep(3)
                    continue
        elif card[-1] == last_card[-1]:
            if player == 1:
                try:
                    player1.put(card)
                    player1_score = player1.calc_score(card)
                    player = 2
                except:
                    print(chr(27) + "[2J")
                    print('The card chosen is not in the deck. If you don\'t have a card of that suit type 2')
                    sleep(3)
                    continue
            else:
                try:
                    player2.put(card)
                    player2_score = player2.calc_score(card)
                    player = 1
                except:
                    print(chr(27) + "[2J")
                    print('The card chosen is not in the deck. If you don\'t have a card of that suit type 2')
                    sleep(3)
                    continue
        else:
            print(chr(27) + "[2J")
            print('You must put a card with the same suit')
            sleep(3)
            continue    
        moves+=1
        last_card = card
    elif action == '2':
        if player == 1:
            player1.take()
        else:
            player2.take()
        continue
    elif action == '--help':
        while True:
            print(chr(27) + "[2J")
            print('''Game Rules:
            - After the 52 card\'s deck is shuffled, the player\'s should take 5 random cards each.
            - The program will choose one of the players randomly and will print a card from the deck
            that will define the suit that is going to start the game.
            - The first player must start the round with a card of the same suit that appears printed
            in the screen.
            - Then the second player must put a card with the same suit as the first player. 
            * If any of the player\'s don\'t have a card of the same suit they must take 
            cards from the deck until a card of the suit need appears. *
            - The player that puts a card with a greater value starts the next round. And in 
            this case they choose with what suit they want to play.
            (the card\'s values from the lowest to the highest are like this:
            "2,3,4,5,6,7,8,9,10,J,Q,K,A")
            - If a player has one card remaining they must win that round, either way the must take
            cards from the deck until they can respond the next round.
            - The game finishes when one player has no cards remaining
                ''')
            resume = input()
            if resume == '--resume':
                break
            else:
                continue
        continue
    else:
        print(chr(27) + "[2J")
        print('Invalid option, please type 1 or 2')
        sleep(2)
        continue
    
    if moves % 2 == 0:
        if player1_score > player2_score:
            message = '{} you won this round'.format(p1)
            print(chr(27) + "[2J")
            print(message)
            player = 1
        else:
            message = '{} you won this round'.format(p2)
            print(chr(27) + "[2J")
            print(message)
            player = 2
        
        sleep(2)
        moves = 0
        last_card = ''
    
    #If deck gets empty append the cards from the pile
    if deck == []:
        deck = cards_pile
        #The top card of the pile won't go to the deck
        deck.remove(last_card)
        cards_pile = []
    