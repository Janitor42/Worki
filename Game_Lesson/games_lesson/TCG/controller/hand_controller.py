from controller.config import *
from gui.card_widget import CardWidget
from logic.card import Card

from logic.creature_card import CreatureCard


class HandController:

    @staticmethod
    def find_card_by_target(target, widget_list):
        for hand_widget in widget_list:
            hand_widget: CardWidget
            if target in hand_widget.draw_widgets:
                card_widget = hand_widget
                return card_widget
        return False

    def __init__(self, player_model, player_gui):
        self._model = player_model
        self.gui = player_gui

    def update_visual(self):
        self.gui.update_visual()
        self.gui.clear_widgets('hand_widgets')
        self.gui.clear_widgets('board_widgets')

        logic_card = self._model.get_attr('hand')
        if logic_card:
            self.collect_view(logic_card=logic_card, atr_frame='frame_hand', atr_list='hand_widgets')

        logic_card = self._model.get_attr('table')
        if logic_card:
            self.collect_view(logic_card=logic_card, atr_frame='frame_board', atr_list='board_widgets')

    def collect_view(self, logic_card, atr_frame, atr_list):
        atr_frame = getattr(self.gui, atr_frame, None)
        atr_list = getattr(self.gui, atr_list, None)
        for index, model_card in enumerate(logic_card):
            card_view = CardWidget(card_logic=model_card, parent_widget=atr_frame)
            x_pos = index * DISTANCE_X + INDENT_X
            card_view.place(x=x_pos, y=INDENT_Y)
            atr_list.append(card_view)

    def card_form_any(self, target, atr):
        atr = getattr(self.gui, atr, [])
        hand_widgets = [x for x in atr]
        card_widget = HandController.find_card_by_target(target=target, widget_list=hand_widgets)
        if card_widget:
            card_widget: CardWidget
            return card_widget.card_logic
        return False

    def can_card_play(self, card):
        if isinstance(card, CreatureCard) and card.get_state_attack():
            return card
        return False

    def get_widget_by_logic(self, card_logic):
        for widget in self.gui.board_widgets:
            if widget.card_logic == card_logic:
                return widget.frame
        return None
