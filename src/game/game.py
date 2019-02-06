from src.dealer import DealerHand
from src.deck import Deck
from src.player import PlayerHand


class Game:

    def __init__(self, dealer=None, player=None, deck=None):
        self.deck = Deck() if not deck else deck
        self.dealer = DealerHand(self.deck) if not dealer else dealer
        self.player = PlayerHand(self.deck) if not player else player
        self.round = 0
        self.game_finished = False

    def round_1(self):
        self.dealer.get_one_card()
        self.player.get_two_cards()
        if self.is_blackjack:
            self.game_finished = True

    def reset_game(self):
        self.dealer.reset_hand()

        self.player.reset_hand()
        self.dealer.reset_hand()

    @property
    def is_blackjack(self):
        if not len(self.player.hand) == 2:
            return False
        return self.player.evaluate_hand()[0] == 21

    def player_lost(self):
        return self.player.lost_game()

    def dealer_lost(self):
        return self.dealer.lost_game()


