from controller.config import *
from gui.card_widget import CardWidget
from gui.player_board import PlayerBoard

class HandController:

    def __init__(self, player_model, player_gui):
        self._model = player_model
        self._gui = player_gui

    def update_hand_view(self):
        self._gui.clear_table_hand()

        logic_cards = self._model.get_attr('hand')
        if not logic_cards:
            return

        for index, model_card in enumerate(logic_cards):

            card_view = CardWidget(card_logic=model_card, parent_widget=self._gui.frame_hand)
            x_pos = index * DISTANCE_X + INDENT_X
            card_view.place(x=x_pos, y=INDENT_Y)

            self._gui.hand_widgets.append(card_view)

