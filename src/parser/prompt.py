import os
import time
from cmd import Cmd

from unicards import unicard

from src.game import Game
from src.parser.utils.is_positive_number import is_positive_number
from src.settings.constants import OS
from src.settings.messages import WELCOME_MESSAGE, DEPOSIT_AMOUNT, \
    NOT_A_POSITIVE_NUMBER, GOODBYE_MESSAGE


class Prompt(Cmd):
    prompt = ''

    def __init__(self, *args, **kwargs):
        super(Prompt, self).__init__(*args, **kwargs)
        self.do_clear()
        self.do_welcome()

    def do_exit(self, inp=None):
        self.do_clear()
        print(GOODBYE_MESSAGE)
        return True

    def do_welcome(self, s=None):
        print(WELCOME_MESSAGE)

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
            time.sleep(.1)
            end_text = f'] {percentage}%'
            final = start_text + new_middle_text + end_text
            self.do_clear()
            print(final)

    def do_clear(self, s=None):
        os.system(OS)

    def validate_data(self,data):
        if data == 'q':
            return self.do_exit()
        if not is_positive_number(data):
            self.do_clear()
            print(NOT_A_POSITIVE_NUMBER)
            return self.do_start()

    def do_start(self,a=None):
        data = input(DEPOSIT_AMOUNT)
        self.validate_data(data)
        game = Game()
        card = game.player.get_one_card()
        # TODO: continue the game here


