import random

from controller.hand_controller import HandController
from logic.card import Card
from logic.player import Player

from gui.card_widget import CardWidget


class AIController:
    def __init__(self, player_model: Player, player_controller: HandController):
        self.player_model = player_model
        self.player_controller = player_controller

    def find_group_card(self, atr):
        return [x for x in self.player_model.get_attr(atr)]

    def find_enemy_cards(self, enemy_player_model):
        enemy_player_model: Player
        enemy_cards = enemy_player_model.get_my_table_cards()
        return enemy_cards

    def ai_choice_attack_creature_to_creature(self, enemy_cards_on_table):
        return random.choice(enemy_cards_on_table)

    # region from hand

    def find_cards_from_hand(self):
        cards = self.find_group_card(atr='hand')
        cards_sorted = sorted(cards, key=lambda x: x.get_attr('_cost'))
        if cards_sorted:
            return cards_sorted[0]
        else:
            return False

    def play_card_from_hand(self, cards):
        if cards.get_attr('_cost') > self.player_model.get_attr('_energy'):
            return False

        self.player_model.remove_and_send_on_table(target=cards.get_attr('_name'))
        self.player_model.set_energy(energy=int(cards.get_attr('_cost')))
        return True

    # endregion

    # region from board

    def find_card_from_board(self):
        cards = self.find_group_card(atr='table')
        cards_sorted = [x for x in cards if x.get_state_attack()]
        if cards_sorted:
            return cards_sorted[0]
        else:
            return False
        # def play_card_from_board(self, cards, enemy_player_model):
        #     enemy_cards_on_table = self.find_enemy_cards(enemy_player_model=enemy_player_model)
        #     if not enemy_cards_on_table:  # атакуем в лицо героя
        #         self.player_model.attack_enemy_hero(
        #             attacked_card_model=target, enemy_player_model=enemy_player_model)
        # else:  # атакуем его существ если они есть
        #     enemy_target = self.ai_choice_attack_creature_to_creature(enemy_cards_on_table=enemy_cards_on_table)
        #     self.player_model.attack_creature_to_creature(
        #         my_creature=target, enemy_creature=enemy_target, enemy_player_model=enemy_player_model)
        return True

    # endregion
