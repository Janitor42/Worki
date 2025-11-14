

import random
all_cards = []


def create_cards():
    colors = ["♥️", "♦️", "♣️", "♠️"]
    names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'K', 'T']
    for color in colors:
        for name in names:
            obj = [color,name]
            all_cards.append(obj)


create_cards()

print(all_cards)
for i in all_cards:
    print(i)