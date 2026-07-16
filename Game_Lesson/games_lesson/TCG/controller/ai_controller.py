from controller.hand_controller import HandController
from logic.card import Card
from logic.player import Player


class AIController:
    def __init__(self, player_model: Player, player_controller: HandController):
        self.player_model = player_model
        self.player_controller = player_controller


    def find_cards(self):
        cards = [x for x in self.player_model.hand]
        cards_sorted = sorted(cards, key=lambda x: x.get_attr('_cost'))
        return cards_sorted

    def try_play_card(self):
        cards = self.find_cards()
        if not cards:
            return False
        target = cards[0]
        if target.get_attr('_cost') > self.player_model.get_attr('_energy'):
            return False

        self.player_model.remove_and_take_from_table(target=target.get_attr('_name'))
        self.player_model.set_energy(energy=int(target.get_attr('_cost')))
        return True
