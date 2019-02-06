from src.settings.constants import NUM_OF_DECK_CARDS, DECK_SPECIAL, DECK_ACE


class BaseHand:
    def __init__(self, deck):
        self.round = 0
        self.deck = deck
        self.hand = []

    def get_one_card(self):
        """
        Draws one card from the deck.
        It is the same deck that is used by the
        both parties as well.
        """
        card = self.deck.get_one_card()
        self.hand.append(card)
        return card

    def transform_cards_to_points(self):
        """
        Method that transorms the flat array of the
        cards to an array of numbers, which indicate the value
        of each card. In addition we have a boolean that
        shows if there is an ace or not.
        """
        points = []
        if not self.hand:
            return points, False
        has_ace = False
        for card in self.hand:
            if card[0] in DECK_SPECIAL:
                points.append(10)
            elif card[0] in DECK_ACE:
                has_ace = True
                points.append(11)
            else:
                points.append(int(card[0]))
        return points, has_ace

    def evaluate_hand(self):
        """
        Method that computes the sum of the cards.
        """
        points, has_ace = self.transform_cards_to_points()

        # Empty hand
        if not points:
            return 0, 0

        if has_ace:
            sum_with_small_ace = sum(
                1 if point == 11 else point
                for point in points
            )
            sum_with_big_ace = sum(
                11 if point == 11 else point
                for point in points
            )
        else:
            sum_with_small_ace = sum(point for point in points)
            sum_with_big_ace = sum_with_small_ace

        return sum_with_big_ace, sum_with_small_ace

    def reset_hand(self):
        """
        Method that resets to empty the hand.
        """
        self.hand = []

    def lost_game(self):
        return min(self.evaluate_hand()) > 21
