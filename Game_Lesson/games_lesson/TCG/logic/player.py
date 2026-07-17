import random
from logic import config
from logic.creature_card import CreatureCard


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
        self.table = []

    def take_damage_hero(self, damage):
        self._hp -= damage

    def draw_card(self):
        if self._deck:
            self.hand.append(self._deck.pop())

    def reset_energy(self):
        self._energy = config.STANDARD_ENERGY_PLAYER

    def reset_attacked_creature_table(self):
        for i in self.table:
            if isinstance(i, CreatureCard):
                i.reset_attacked()

    def get_attr(self, atr):
        return getattr(self, atr, None)

    def begin_round(self):
        self.reset_energy()
        self.reset_attacked_creature_table()
        if not len(self._deck) > config.MAX_CARDS_ON_TABLE:
            return False
        target = config.MAX_CARDS_ON_TABLE - len(self.hand)
        for i in range(target):
            self.draw_card()
        return True

    def set_energy(self, energy):
        self._energy -= energy

    def check_card_to_play(self, card_logic):
        price = card_logic.get_attr('_cost')
        name = card_logic.get_attr('_name')
        if self._energy >= price:
            self.set_energy(energy=price)
            self.remove_and_take_from_table(target=name)
            return True
        return False

    def remove_and_take_from_table(self, target):
        for index, obj in enumerate(self.hand):
            name = obj.get_attr('_name')
            if target == name and Player.get_creature(obj):
                self.table.append(self.hand.pop(index))
                return
            if target == name and not Player.get_creature(obj):
                self.hand.remove(obj)
                return

    def attack_enemy_hero(self, attacked_card_model, enemy_player_model):
        attacked_card: CreatureCard
        enemy_player_model: Player

        damage = attacked_card_model.get_attr('_attack_power')
        enemy_player_model.take_damage_hero(damage=damage)
        attacked_card_model.disabled_attack()

    def attack_creature_to_creature(self, my_creature, enemy_creature):
        my_creature: CreatureCard
        enemy_creature: CreatureCard
        my_hit = my_creature.calculate_damage(enemy_element=enemy_creature.get_attr('_element'))
        enemy_creature.take_damage(damage=my_hit)
        enemy_hit = enemy_creature.calculate_damage(enemy_element=my_creature.get_attr('_element'))
        my_creature.take_damage(damage=enemy_hit)
        my_creature.disabled_attack()
