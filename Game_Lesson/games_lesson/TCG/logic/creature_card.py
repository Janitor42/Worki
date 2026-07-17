from logic.card import Card
from logic import config


class CreatureCard(Card):
    def __init__(self, name, cost, element, attack_power, hp, keywords):
        super().__init__(name, cost)
        self._element = element
        self._attack_power = attack_power
        self._hp = hp
        self._keywords = keywords
        self._has_attacked = config.CHARGE in self._keywords

    def reset_attacked(self):
        self._has_attacked = True

    def calculate_damage(self, enemy_element):
        target = config.ELEMENT_ADVANTAGES.get(self._element)
        print(self._element)
        if target == enemy_element:
            return self._attack_power + config.ELEMENT_BONUS_DAMAGE
        return self._attack_power

    def take_damage(self, damage):
        self._hp -= damage

    def get_attr(self, attr):
        return getattr(self, attr, None)

    def get_state_attack(self):
        return self._has_attacked

    def disabled_attack(self):
        self._has_attacked = False