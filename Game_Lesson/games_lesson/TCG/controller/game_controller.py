import random

from dataclasses import dataclass

from gui.player_panel import PlayerPanel
from gui.game_field import GameField
from gui.card_widget import CardWidget

from controller.hand_controller import HandController
from controller.ai_controller import AIController


class GameController:
    @dataclass
    class Views:
        player_gui: PlayerPanel
        bot_gui: PlayerPanel
        game_field: GameField

    def __init__(self, player_model, bot_model, views: Views):
        self._player_model = player_model
        self._bot_model = bot_model

        self.player_gui = views.player_gui
        self.bot_gui = views.bot_gui
        self.game_field = views.game_field

        self._is_player_turn = random.choice([True, False])

        self.player_controller = HandController(player_model=self._player_model, player_gui=self.player_gui)
        self.player_controller.update_visual()

        self.bot_controller = HandController(player_model=self._bot_model, player_gui=self.bot_gui)
        self.bot_controller.update_visual()
        self.ai_boot = AIController(player_model=bot_model, player_controller=self.bot_controller)

        self.game_field.end_turn_btn.config(command=self.end_turn_action)
        self.game_field.root.bind('<ButtonPress-1>', self.human_turn)

        if not self._is_player_turn:
            self.game_field.root.after(1000, self.ai_turn)

    def end_turn_action(self):
        if self._is_player_turn:
            self._player_model.begin_round()
            self.player_controller.update_visual()
            self._is_player_turn = False
            self.game_field.turn_off_interface()
            self.game_field.root.after(1000, self.ai_turn)

    def ai_turn(self):
        if self._is_player_turn:
            return
        try_played = self.ai_boot.try_play_card()
        if try_played:
            self.bot_controller.update_visual()
            self.game_field.root.after(1000, self.ai_turn)
        else:
            self._bot_model.begin_round()
            self.bot_controller.update_visual()
            self.game_field.bot_speak_end_turn_action()
            self.game_field.turn_on_interface()
            self._is_player_turn = True




    def human_turn(self, event):
        if not self._is_player_turn:
            return

        target = event.widget
        hand_widgets = [x for x in self.player_gui.hand_widgets]
        card_widget = False

        for hand_widget in hand_widgets:
            hand_widget: CardWidget
            if target in hand_widget.get_draw_obj():
                card_widget = hand_widget
                break

        if not card_widget:
            return
        card_widget: CardWidget

        if self._player_model.check_card_to_play(obj=card_widget):
            self.player_controller.update_visual()
        else:
            self.game_field.no_enough_energy_action()
