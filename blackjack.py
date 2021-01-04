# MADY BY: Lisette Spalding
# DATE CREATED: 01-04-2021
# DATE LAST MODIFIED: 01-04-2021
# Blackjack

import random
import cards as m_cards
import game_func

class BJ_Cards(m_cards.Pos_Card):
    ACE_VALUE = 1

    @property

    def value(self):
        if self.isFaceUp:
            V = BJ_Cards.RANKS.index(self.rank)+1
            if V > 10:
                V = 10
        else:
            V = None
        return V

class BJ_Deck(m_cards.Deck):
    def populate(self):
        for suit in BJ_Cards.SUITS:
            for rank in BJ_Cards.RANKS:
                self.cards.append(BJ_Cards(rank, suit))


deck = BJ_Deck()
deck.populate()
deck.shuffle()
print(deck.cards[0])