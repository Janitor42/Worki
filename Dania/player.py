import random as rd

from deck import Desk


class Player:
    hand = []

    @classmethod
    def give_card(cls):
        keys=list(Desk.pack.keys())
        key=rd.choice(keys)
        card = Desk.pack[key]

        Player(color=card.color, value=card.value)

    def __init__(self, color, value):
        self.color = color
        self.value = value
        Player.hand.append(self)
        Desk.remove_card(f'{self.color}{self.value}')

