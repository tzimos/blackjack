import copy
from random import random

from src.settings.constants import COMPLETE_DECK_FLAT


def refresh_deck(cls):
    """
    Decorator for refreshing the deck every time that the cards are
    finished.
    """

    class Wrapper():
        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            length_of_deck = len(self.wrapped.current_deck)
            if length_of_deck == 0:
                self.wrapped.current_deck = self.wrapped.get_refreshed_flat_deck()

            return getattr(self.wrapped, name)

    return Wrapper
