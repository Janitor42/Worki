from logic.card import Card
from logic import config


class CreatureCard(Card):
    def __init__(self, name, cost, element, attack_power, hp):
        super().__init__(name, cost)
        self._element = element
        self._attack_power = attack_power
        self._hp = hp

    def calculate_damage(self, enemy_element):
        target = config.ELEMENT_ADVANTAGES.get(self._element)
        if target == enemy_element:
            return self._attack_power + config.ELEMENT_BONUS_DAMAGE
        return self._attack_power

    def take_damage(self, amount):
        self._hp -= amount
