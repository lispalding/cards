# MADE BY: Lisette Spalding
# DATE CREATED: 12/17/2020
# DATE LAST MODIFIED: 12/17/2020
#### Cards starting module ####

##################### IMPORTS #####################
import random
####################### FIN #######################

##################### CLASSES #####################
class Card(object): # Creating a class called "Card"
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["♥", "♦","♣","♠"]

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = str.format("""
        +----------+
        | {0:<2}{1}      |
        |          |
        |          |
        |          |
        |     {1}{0:>2}  |
        +----------+
        """, self.rank, self.suit)
        return rep

class Pos_Card(Card):
    def __init__(self, rank, suit, faceUp=True):
        super(Pos_Card, self).__init__(rank, suit)
        self.isFaceUp = faceUp

    def __str__(self):
        if self.isFaceUp:
            rep = super(Pos_Card, self).__str__()

        else:
            rep = str.format("""
                        +----------+
                        | ******** |
                        | ******** |
                        | ******** |
                        | ******** |
                        | ******** |
                        +----------+
                        """, self.rank, self.suit)
        return rep

    def flip(self):
        self.isFaceUp = not self.isFaceUp

class Hand(object): # Creating a class called "Hand"
    def __init__(self): # Defining the self
        self.cards = []

    def __str__(self): # Creating a way to show cards in hand
        rep = ""
        if self.cards: #Sayiing that if there is a card in the hand (Or if there isn't), then return this
            for card in self.cards:
                rep += str(card)
        else:
                rep = "< EMPTY >"
        return rep

    def clear(self): # Clearing hand
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self,card,otherHand):
        self.cards.remove(card)
        otherHand.add(card)

class Deck(Hand):
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self,handsList,perHand=1):
        for rounds in range(perHand):
            for hand in handsList:
                if self.cards:
                    topCard = self.cards[0]
                    self.give(topCard,hand)
                else:
                    print("Out of cards!")
                    for hand in handsList:
                        hand.clear()
                    self.clear()
                    self.populate()
                    self.shuffle()
                    self.deal(handsList,perHand)

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))

####################### FIN #######################

if __name__ == "__main__":
    print("This is a module with classes for playing cards, not meant to be ran on it's own.")
    input("\n\n Press the enter key to exit.")