values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']
colors = ['♥️', '♦️', '♣️', '♠️']


def create_desk():
    for value in values:
        for color in colors:
            Desk(color=color, value=value)


class Desk:
    # firs - it's color, second it's value
    pack = {}

    @classmethod
    def remove_card(cls, data):
        cls.pack.pop(data)

    def __init__(self, color, value):
        self.color = color
        self.value = value
        Desk.pack[f'{self.color}{self.value}'] = self
