from src.base import BaseHand


class PlayerHand(BaseHand):

    def __init__(self, *args, balance=0):
        super(PlayerHand, self).__init__(*args)
        self.balance = balance

    def get_two_cards(self):
        """
        Draws two cards from the deck.
        It is the same deck that is used by the
        dealer as well.
        """
        cards = self.deck.get_two_cards()
        self.hand.extend(cards)
        return cards

    def increase_balance(self, amount):
        self.balance += amount

    def reset_balance(self):
        self.balance = 0
