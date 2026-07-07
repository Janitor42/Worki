import json
from logic.creature_card import CreatureCard
from logic.spell_card import SpellCard


def load_deck_from_json(json_file):
    data = open(json_file, 'r', encoding="utf-8")

    file = json.load(data)
    data.close()

    deck = []
    for i in file:
        if i['type'] == 'creature':
            target = CreatureCard(name=i['name'], cost=i['cost'], element=i['element'], attack_power=i['attack_power'],
                                  hp=i['hp'])
            deck.append(target)
        elif i['type'] == 'spell':
            target = SpellCard(name=i['name'], cost=i['cost'], spell_type=i['spell_type'], power=i['power'])
            deck.append(target)

    return deck
