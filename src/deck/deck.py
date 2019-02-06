import copy
import random

from src.deck.decorators.refresh_deck import refresh_deck
from src.settings.constants import NUM_OF_DECK_CARDS, COMPLETE_DECK_FLAT



@refresh_deck
class Deck:
    """
    The Deck class which is responsible for common behaviours
    of the deck, such is shuffling the cards.
    """

    def __init__(self):
        self.num_of_deck_cards = NUM_OF_DECK_CARDS
        self.current_deck = copy.copy(COMPLETE_DECK_FLAT)

    def get_one_card(self):
        """Gets one card from the deck."""
        choice = random.choice(self.current_deck)
        self.current_deck.remove(choice)
        return choice

    def get_two_cards(self):
        """Convenience player specific card drawing method"""
        choice1 = self.get_one_card()
        choice2 = self.get_one_card()
        return choice1, choice2

    def get_refreshed_flat_deck(self):
        """
        Copies a flat deck in order to refresh the deck
        completely. Used to avoid IndexError when the deck is
        run out of cards.
        """
        cp_deck_flat = copy.copy(COMPLETE_DECK_FLAT)
        random.shuffle(cp_deck_flat)
        return cp_deck_flat

    def reset_deck(self):
        self.current_deck = self.get_refreshed_flat_deck()