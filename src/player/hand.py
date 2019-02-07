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

    def player_has(self):
        return "Player has: \r\n" + self.show_hand()

    def calc_balance(self, is_blackjack=False, win=False):
        if is_blackjack and not win:
            raise ValueError("You cannot have blackjack and not winning")
        if not any([is_blackjack, win]):
            self.balance = 0
        if win:
            if is_blackjack:
                self.balance *= 2.5
            else:
                self.balance *= 2
        return self.balance
