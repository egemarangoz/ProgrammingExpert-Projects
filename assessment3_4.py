"""
Assessment 3.4 - Deck Class

Create a "Deck" class that represents a deck of 52 playing cards. The "Deck" should maintain which cards are currently in the deck and
never contain duplicated cards. Cards should be represented by a string contatining their value (2-10, J, Q, K, A) followed by their suit
(D, H, C, S). For example, the jack of clubs would be represented by "JC" and the three of hearts would be represented by "3H".

Your "Deck" class should implement the following methods:

- shuffle(): This method shuffles the cards randomly, in place. You may use the "random_shuffle()" method to help you do this.

- deal(n): This method removes and returns the last n cards from the deck in a list. If the deck does not contain enough cards it returns
all the cards in the deck.

- sort_by_suit(): This method sorts the cards by suit, placing all the hearts first, diamonds second, clubs third and spades last. The order
within each suit (i.e. the card values) does not matter. This method should sort the cards in place, it does not return anything.

- contains(card): This method returns "True" if the given card exists in the deck and "False" otherwise.

- copy(): This method returns a new "Deck" object that is a copy of the current deck. Any modifications made to the new "Deck" object
should not affect the "Deck" object that was copied.

- get_cards(): This method returns all the cards in the deck in a list. Any modifications to the returned list should not change the 
"Deck" object.

- __len__(): This method returns the number of the cards in the "Deck".
"""
import random

class Deck:
    # Write your code here.
    suits = ["D", "H", "C", "S"]
    values = [str(i) for i in range (2,11)] + ["J", "Q", "K", "A"]

    def __init__(self):
        self.cards = [Deck.suits[i] + Deck.values[j] for i in range(len(Deck.suits)) for j in range(len(Deck.values))]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        dealt_cards = []
        for i in range(n):
            if len(self.cards) == 0:
                break
    
        card = self.cards.pop()
        dealt_cards.append(card)

    def sort_by_suit(self):
        suit_order = ["H", "D", "C", "S"]
        self.cards = [Deck.suit_order[i] + Deck.values[j] for i in range(len(Deck.suit_order)) for j in range(len(Deck.values))]

    def contains(self, card):
        return card in self.cards

    def copy(self):
        new_deck = Deck()
        new_deck.cards = self.cards[:]
        return new_deck

    def get_cards(self):
        return self.cards[:]

    def __len__(self):
        return len(self.cards)

deck1 = Deck()
print(deck1.contains("3H"))