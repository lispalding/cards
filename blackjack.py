# MADY BY: Lisette Spalding
# DATE CREATED: 01/04/2021
# DATE LAST MODIFIED: 01-06-2021
## !! Blackjack !! ##

##################### IMPORTS #####################
import random
import cards as mCards
import game_func as gf
####################### FIN #######################

##################### CLASSES #####################
class BJ_Cards(mCards.Pos_Card):
    ACE_VALUE = 1 # Setting the Ace's value to one

    @property # Assigning the next function as a property
    def value(self): # Defining a class named value
        """ This function lets the cards be face up or face down, as well as calculating the value.
         To use: BJ_Cards.value() """

        if self.isFaceUp:
            V = BJ_Cards.RANKS.index(self.rank)+1
            if V > 10:
                V = 10
        else:
            V = None
        return V

class BJ_Deck(mCards.Deck):
    def populate(self): # Creating another function, this time named populate
        """ This function appends a card to a hand.
         To use: BJ_Deck.populate() """
        for suit in BJ_Cards.SUITS:
            for rank in BJ_Cards.RANKS:
                self.cards.append(BJ_Cards(rank, suit))

class BJ_Hand(mCards.Hand):
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        """ A str function that will print the cards in your hand. """
        rep = ""

        for i in range(len(self.cards)):
            print(self.cards[i])

        rep = self.name + ":\n" + "Total: " + str(self.total)
        return rep

    @property # Assigning the next function as a property
    def total(self):
        """ This function will total up the values of the cards in your hand.
         To use: BJ_Hand.total() """
        # If a card in the hand has a value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None

        # Add up card values, treat each Ace as a one (1)
        t = 0
        for card in self.cards:
            t+= card.value

        # Determining if the hand contains an Ace
        aceInHand = False
        for card in self.cards:
            if card.rank == BJ_Cards.ACE_VALUE:
                aceInHand = True

        if aceInHand and t <= 11:
            t+=10
        return t

    def isBusted(self):
        """ Determining if you have busted with the total in your hand.
         To use: BJ_Hand.isBusted() """
        return self.total > 21


class BJ_Player(BJ_Hand):

    #### FUNCTIONS FOR IF THE PLAYER MEETS A CIRCUMSTANCE

    def isHitting(self):
        response = gf.askYesNo(self.name+"Do you want a hit? (Y/N):  ")
        return response == "y"

    def bust(self):
        print(self.name, "busts...")
        self.lose()

    def lose(self):
        print(self.name, "loses...")

    def win(self):
        print(self.name, "wins.")

    def push(self):
        print(self.name, "pushes.")

class BJ_Dealer(BJ_Hand):
    def isHitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts...")

    def flipFirstCard(self):
        self.cards[0].flip()

class BJ_Game(object):
    def __init__(self,names):
        self.players = []
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

        self.dealer = BJ_Dealer("Dealer")

        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

    @property
    def stillPlaying(self):
        sp = []
        for player in self.players():
            if not player.isBusted():
                sp.append(player)
        return sp

    def __additonalCards(self,player):
        while not player.isBusted() and player.isHitting():
            self.deck.deal([player],1)
            print(player)
            if player.isBusted():
                player.bust()

    def play(self):
        self.deck.deal(self.players+[self.dealer],perHand=2)
        self.dealer.flipFirstCard()
        for player in self.players:
            print(player)
        print(self.dealer)

        for player in self.players:
            self.__additonalCards(player)

        self.dealer.flipFirstCard()

        if not self.stillPlaying:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additonalCards(self.dealer)

            if self.dealer.isBusted():
                for player in self.stillPlaying:
                    player.win()
            else:
                for player in self.stillPlaying:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
            for player in self.players:
                player.clear()
                self.dealer.clear()

####################### FIN #######################

def main():
    print("\t\tWelcome to Blackjack!\n")

    names = []
    number = gf.getNumber(7, 1, "How many players? (1-7):  ")
    for i in range(number):
        name = input("Enter player name:  ")
        names.append(name)

    game = BJ_Game(names)
    again = None
    while again != "n":
        game.play()
        again = gf.askYesNo("\nDo you want to play again?: ")

#### CALLING MAIN ####
main()