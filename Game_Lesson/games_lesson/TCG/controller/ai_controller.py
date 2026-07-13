class AIController:
    def __init__(self, player_model, player_controller):
        self.player_model = player_model
        self.player_controller = player_controller

    def think(self):
        cards = self.find_cards()
        for i in cards:
            print(i.__dict__)

    def find_cards(self):
        cards = [x for x in self.player_model.hand]
        cards_sorted = sorted(cards, key=lambda x: x.get_attr('_cost'), reverse=True)
        return cards_sorted
