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
        return {
            'dealer': self.dealer.hand,
            'player': self.player.hand,
            'is_blackjack': self.is_blackjack,
            'dealer_has': self.dealer.dealer_has(),
            'player_has': self.player.player_has()
        }

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

    def is_finished(self):
        return self.player.lost_game() \
               or self.dealer.lost_game() \
               or not self.dealer_must_continue()

    def winner(self):
        if self.player.best_evaluation() <= self.dealer.best_evaluation():
            return 'dealer'
        else:
            if self.is_blackjack:
                self.player.balance *= 2.5
            else:
                self.player.balance *= 2
            return 'player'


    def dealer_must_continue(self):
        hand = self.dealer.evaluate_hand()
        minimun = min(hand)
        maximum = max(hand)
        if self.dealer.best_evaluation() < self.player.best_evaluation():
            return True
        elif self.dealer.best_evaluation() >= self.player.best_evaluation():
            return False

        if (minimun >= 17 or maximum >= 17):
            return False

        return True
