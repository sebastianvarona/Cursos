from random import shuffle, randint
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
    def __init__(self):
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
            message = 'There\'s a winner'
            win = True
        return message
deck = create_deck()
player = Player()
print(player.hand)

