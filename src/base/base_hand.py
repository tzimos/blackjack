import time

from src.settings.constants import NUM_OF_DECK_CARDS, DECK_SPECIAL, DECK_ACE, \
    CARD_DECK_SYMBOLS


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
            if len(card) == 3:
                cp = card[:]
                card = [None] * 2
                card[0] = cp[:2]
                card[1] = cp[-1]
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

    def _construct_card(self, card):
        c = ' -------\r\n' \
            '|{num}     |\r\n' \
            '|       |\r\n' \
            '|   {symbol}   |\r\n' \
            '|       |\r\n' \
            '|     {num}|\r\n' \
            ' -------\r\n'

        if len(card) == 2:
            num = card[0] + ' '
            symbol_ = card[1]
        else:
            num = card[:2]
            symbol_ = card[-1]

        symbol = CARD_DECK_SYMBOLS[symbol_]

        card = c.format(num=num, symbol=symbol)

        return card

    def _append_cards(self, hand):
        """
        Given an array of the hand of a participant in the game
        it returns the graphical display of the currnet cards.

        :param hand: the current hand of a participant in the game.
        :type list

        :return: str
        """
        sep = '\r\n'
        raw_list_of_cards = []
        for card in hand:
            raw_list_of_cards.append(self._construct_card(card))
        raw_list = list(map(lambda x: x.split(sep), raw_list_of_cards))

        first_line = []
        second_line = []
        third_line = []
        forth_line = []
        fifth_line = []
        sixth_line = []
        last_line = []
        for element in raw_list:
            first_line.append(element[0] + '  ')
            second_line.append(element[1] + ' ')
            third_line.append(element[2] + ' ')
            forth_line.append(element[3] + ' ')
            fifth_line.append(element[4] + ' ')
            sixth_line.append(element[5] + ' ')
            last_line.append(element[6] + '  ')

        first_l = ''.join(first_line)
        second_l = sep + ''.join(second_line)
        third_l = sep + ''.join(third_line)
        forth_l = sep + ''.join(forth_line)
        fifth_l = sep + ''.join(fifth_line)
        sixth_l = sep + ''.join(sixth_line)
        last_l = sep + ''.join(last_line)
        return first_l + second_l + third_l + forth_l + fifth_l + sixth_l + last_l

    def show_hand(self):
        return self._append_cards(self.hand) + self.evaluate_hand_for_gui()

    def evaluate_hand_for_gui(self):
        hand = self.evaluate_hand()
        minimum = min(hand)
        maximum = max(hand)
        if minimum == maximum or maximum > 21:
            return f'Sum of cards {minimum}'
        return f'Sum of cards minimum:{minimum}, maximum:{maximum}'

    def best_evaluation(self):
        hand = self.evaluate_hand()
        minimum = min(hand)
        maximum = max(hand)
        if minimum > 21:
            return 0
        if minimum == maximum:
            return minimum
        if maximum > 21:
            return minimum
        else:
            return maximum
