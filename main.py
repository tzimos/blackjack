from src.dealer.hand import DealerHand
from src.deck import Deck
from src.parser import Prompt

Prompt().cmdloop()
# from src.player.hand import PlayerHand
#
# deck = Deck()
# player = PlayerHand(deck)
# dealer = DealerHand(deck)
#
# player.get_one_card()
# player.get_one_card()
# player.get_one_card()
# dealer.get_one_card()
# player.get_two_cards()
# print(player.hand)
# print(player.evaluate_hand())
# print(player.lost_game())