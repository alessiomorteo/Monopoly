from random import shuffle

class CardDeck:
    def __init__(self, card_set:dict)->None:
        """Initialise a class that represents a deck of cards.
        """
        self.card_set = shuffle(card_set) # random shuffling of the deck

    def add_card(self, card)->None:
        """Function to handle the addition of a card to the top of the deck.

        Args:
            card (SpecialCard): An instance of the special card parent class.
        """
        self.card_set.insert(0, card)

    def pick_card(self):
        """Function to handle the picking up of a card from the
        top of the deck.
        """
        return self.card_set.pop(-1) # pick the top card of the deck

    def return_card(self, card)->None:
        """Return a removed card to the bottom of the deck.

        Args:
            card (SpecialCard): An instance of the special card parent class.
        """
        self.add_card(card) # put the card to the bottom of the pile
