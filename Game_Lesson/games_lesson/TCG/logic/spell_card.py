from logic.card import Card


class SpellCard(Card):
    def __init__(self, name, cost, spell_type, power):
        super().__init__(name, cost)
        self._spell_type = spell_type
        self._power = power
