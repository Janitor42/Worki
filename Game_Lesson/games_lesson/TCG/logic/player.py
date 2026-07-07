import random
from logic import config


class Player:

    def __init__(self, name, full_deck):
        self._name = name
        self._hp = config.STANDARD_HP_PLAYER
        self._energy = config.STANDARD_ENERGY_PLAYER
        self._deck = full_deck.copy()
        random.shuffle(self._deck)
        self._hand = []
        self._table = []

    def draw_card(self):
        if self._deck:
            self._hand.append(self._deck.pop())

    def reset_energy(self):
        self._energy = config.STANDARD_ENERGY_PLAYER

    def get_attr(self, atr):
        return getattr(self, atr, None)

    def take_four_cards(self):
        if not len(self._deck) > 4:
            return False
        for i in range(4):
            self.draw_card()
        return True
