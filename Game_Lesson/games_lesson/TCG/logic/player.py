import random
from logic import config


class Player:
    @staticmethod
    def get_creature(target):
        from logic.creature_card import CreatureCard
        if isinstance(target, CreatureCard):
            return True
        return False

    def __init__(self, name, full_deck):
        self._name = name
        self._hp = config.STANDARD_HP_PLAYER
        self._energy = config.STANDARD_ENERGY_PLAYER
        self._deck = full_deck.copy()
        random.shuffle(self._deck)
        self.hand = []
        self._table = []

    def draw_card(self):
        if self._deck:
            self.hand.append(self._deck.pop())

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

    def set_energy(self, energy):
        self._energy -= energy

    def check_card_to_play(self, obj):
        price = obj.get_price()
        name = obj.get_name()
        if self._energy >= price:
            self.set_energy(energy=price)
            self.remove_and_take_from_table(target=name)
            return True
        return False

    def remove_and_take_from_table(self, target):
        for index, obj in enumerate(self.hand):
            name = obj.get_attr('_name')
            if target == name and Player.get_creature(obj):
                self._table.append(self.hand.pop(index))
                return
            if target == name and not Player.get_creature(obj):
                self.hand.remove(obj)
                return
