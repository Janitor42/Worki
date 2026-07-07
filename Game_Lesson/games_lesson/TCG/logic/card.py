class Card:
    def __init__(self, name, cost):
        self._name = name
        self._cost = cost

    def get_attr(self, atr):
        return getattr(self, atr, None)
