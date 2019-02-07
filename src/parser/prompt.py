import os
import time
from cmd import Cmd
from functools import wraps

from src.game import Game
from src.parser.utils.is_positive_number import is_positive_number
from src.settings.constants import OS, SHUFFLING_SLEEP
from src.settings import messages as msg


def check_balance(f):
    @wraps(f)
    def wrapper(*args):
        instance = args[0]
        player = instance.player
        return f(*args)

    return wrapper


class Prompt(Cmd):
    prompt = ''

    def __init__(self, *args, **kwargs):
        super(Prompt, self).__init__(*args, **kwargs)
        self.game = None
        self.dealer = None
        self.player = None
        self.do_clear()
        self.do_welcome()
        self.plays_next = None

    def do_exit(self, inp=None):
        self.do_clear()
        print(msg.GOODBYE_MESSAGE)
        quit()

        return True

    def do_welcome(self, s=None):
        print(msg.WELCOME_MESSAGE)
        return self.do_after_welcome()

    def do_after_welcome(self, a=None):
        data = input()
        if data == '':
            return self.do_start()
        else:
            self.do_clear()
            self.do_after_welcome()

    def do_shuffling_deck(self, un=None):
        """
        Graphic extra to show to the player that the dealer is
        shuffling the cards.
        """
        end = 20
        start_text = 'Shuffling ['
        middle_text = '_' * end

        for idx, text in enumerate(middle_text, start=1):
            start = idx
            percentage = round((start / end) * 100, 1)

            middle_text_list = list(middle_text)
            middle_text_list[:idx] = '=' * (idx + 1)
            new_middle_text = ''.join(middle_text_list)
            time.sleep(SHUFFLING_SLEEP)
            end_text = f'] {percentage}%'
            final = start_text + new_middle_text + end_text
            self.do_clear()
            print(final)

    def do_clear(self, s=None):
        os.system(OS)

    def validate_data(self, data):
        if data == 'q':
            return self.do_exit()
        if not is_positive_number(data):
            self.do_clear()
            print(msg.NOT_A_POSITIVE_NUMBER)
            return self.do_start()
        return int(data)

    def do_ask_reset(self, a=None):
        data = input(msg.ASK_RESET_GAME)
        if data == '':
            self.do_reset_game()
        else:
            self.do_clear()
            self.do_after_welcome()

    def do_show_winner(self, a=None):
        winner = self.game.winner()
        print(msg.AND_THE_WINNER_IS.format(winner))
        if winner is 'player':
            print('\n' + msg.AMOUNT_WON.format(self.player.balance))
        print('\n\n\n')
        self.do_play_again()

    def do_play_again(self):
        data = input(msg.ASK_TO_PLAY_AGAIN)
        if data == 'q':
            self.do_exit()
        if data == '':
            self.do_clear()
            self.do_reset_game()

    @check_balance
    def do_hit(self, player=None):
        if player:
            self.player.get_one_card()
            self.do_show_hands()
            if self.game.is_finished():
                self.do_show_winner()
                self.do_ask_reset()
            self.do_ask_hit_or_stand()
        else:
            self.dealer.get_one_card()
            self.do_show_hands()
            if self.game.is_finished():
                self.do_show_winner()
                self.do_ask_reset()
            self.do_dealer_thinks_to_continue()

    def do_dealer_thinks_to_continue(self):
        time.sleep(1)
        go_on = self.game.dealer_must_continue()
        if go_on:
            self.do_hit(False)
        else:
            self.do_show_winner()

    @check_balance
    def do_stand(self, player=None):
        self.do_dealer_thinks_to_continue()

    def do_ask_hit_or_stand(self, player=None):
        response = self._do_ask_hit_or_stand()
        response = self.validate_data(response)
        if response == 1:
            self.do_hit(True)
        elif response == 2:
            self.do_stand(player)
        else:
            self.do_ask_hit_or_stand()

    def _do_ask_hit_or_stand(self, a=None):
        return input(msg.HIT_OR_STAND)

    def do_ask_top_up(self, a=None):
        return input(msg.DEPOSIT_AMOUNT)

    def do_show_hands(self):
        print(self.dealer.dealer_has())
        print(self.player.player_has())

    def do_reset_game(self, a=None):
        # Ask the user to input an amount to bet.
        amount = self.do_ask_top_up()
        amount = self.validate_data(amount)
        self.game = Game()
        self.player = self.game.player
        self.dealer = self.game.dealer
        self.plays_next = 'player'

        self.player.balance += amount

        # Shuffling deck
        self.do_shuffling_deck()

        dict_ = self.game.round_1()
        is_blackjack = dict_['is_blackjack']
        self.do_show_hands()

        if is_blackjack:
            balance = self.game.player.calc_balance()
            self.do_blackjack_msg()

        self.do_ask_hit_or_stand()

    def do_blackjack_msg(self):
        print(msg.BLACKJACK_MSG.format(self.player.balance))
        self.do_ask_reset()

    def do_start(self, a=None):
        self.do_reset_game()
