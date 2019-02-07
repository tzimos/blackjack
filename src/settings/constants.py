import itertools
import os

OS = 'cls' if os.name == 'nt' else 'clear'
PROMPT = '(testing)'

NUM_OF_DECK_CARDS = 52
INITIAL_STAKE = 0
DECK_SUITS = ['c', 'd', 'h', 's']
DECK_SPECIAL = ['J', 'Q', 'K']
DECK_ACE = ['A',]
DECK_NUMBERS = tuple([str(num) for num in range(2, 11)] + DECK_SPECIAL+ DECK_ACE)
COMPLETE_DECK = [
    [
        number + suit
        for number in DECK_NUMBERS
    ]
    for suit in DECK_SUITS
]

COMPLETE_DECK_FLAT = list(itertools.chain.from_iterable(COMPLETE_DECK))

CARD_DECK_SYMBOLS_ = ['♣','♦','♥','♠']
CARD_DECK_SYMBOLS = dict(zip(DECK_SUITS, CARD_DECK_SYMBOLS_))
SHUFFLING_SLEEP = 0.001