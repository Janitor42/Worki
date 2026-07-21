from dataclasses import dataclass

from gui.player_panel import PlayerPanel
from gui.game_field import GameField
from gui.card_widget import CardWidget

from controller.hand_controller import HandController
from controller.ai_controller import AIController


class GameController:
    @staticmethod
    def find_card_by_target(target, widget_list):
        for hand_widget in widget_list:
            hand_widget: CardWidget
            if target in hand_widget.get_draw_obj():
                card_widget = hand_widget
                return card_widget
        return False

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

        # self._is_player_turn = random.choice([True, False])
        self._is_player_turn = True

        self.player_controller = HandController(player_model=self._player_model, player_gui=self.player_gui)
        self.player_controller.update_visual()

        self.bot_controller = HandController(player_model=self._bot_model, player_gui=self.bot_gui)
        self.bot_controller.update_visual()
        self.ai_boot = AIController(player_model=bot_model, player_controller=self.bot_controller)

        self.game_field.end_turn_btn.config(command=self.end_turn_action)
        self.game_field.root.bind('<ButtonPress-1>', self.human_turn)

        self.selected_creature_model = None

        if not self._is_player_turn:
            self.game_field.root.after(1000, self.ai_turn)

    def end_turn_action(self):
        if self._is_player_turn:
            self._player_model.begin_round()
            self.player_controller.update_visual()
            self._is_player_turn = False
            self.game_field.turn_off_interface()
            self.game_field.root.after(1000, self.ai_turn)
            self.selected_creature_model = False

    # region bot
    def ai_turn(self):
        self.player_controller.update_visual()
        self.bot_controller.update_visual()
        if self._is_player_turn:
            return
        card_from_hand = self.ai_boot.play_card_from_hand()
        card_from_table = self.ai_boot.play_card_from_table(enemy_player_model=self._player_model)
        if card_from_hand:
            self.game_field.root.after(1000, self.ai_turn)
        elif card_from_table:
            self.game_field.root.after(1000, self.ai_turn)
        else:
            self._bot_model.begin_round()
            self.bot_controller.update_visual()
            self.game_field.bot_speak_end_turn_action()
            self.game_field.turn_on_interface()
            self._is_player_turn = True

    # endregion

    # region human
    def human_turn(self, event):
        if not self._is_player_turn:
            return
        target = event.widget

        if self.selected_creature_model:
            if self.creature_hit_enemy_hero(target=target):
                return
            if self.creature_hit_creature_enemy(target=target):
                return
        self.selected_creature_model = None

        if self.play_form_hand(target=target):
            return
        if self.play_form_board(target=target):
            return


    def play_form_hand(self, target):
        hand_widgets = [x for x in self.player_gui.hand_widgets]
        card_widget = GameController.find_card_by_target(target=target, widget_list=hand_widgets)
        if card_widget:
            card_widget: CardWidget
            if self._player_model.check_card_to_play(card_logic=card_widget.card_logic):
                self.player_controller.update_visual()
            else:
                self.game_field.information_action(text='Недостаточно энергии')
            return True
        return False

    def play_form_board(self, target):
        board_widgets = [x for x in self.player_gui.board_widgets]
        card_widget = GameController.find_card_by_target(target=target, widget_list=board_widgets)
        if card_widget:
            self.selected_creature_model = card_widget.card_logic
            self.information_about_your_choice()
            return True
        return False

    def information_about_your_choice(self):
        if self.selected_creature_model.get_state_attack():
            self.game_field.information_action(
                text=f'Вы выбрали {self.selected_creature_model.get_attr("_name")}, кого атакуете?')
        else:
            self.game_field.information_action(text=f'существо не может атаковать')
            self.selected_creature_model = None

    def creature_hit_enemy_hero(self, target):
        hero_widgets = self.bot_gui.get_draw_obj()
        if target in hero_widgets:
            self._player_model.attack_enemy_hero(attacked_card_model=self.selected_creature_model,
                                                 enemy_player_model=self._bot_model)
            self.bot_controller.update_visual()
            self.selected_creature_model = False
            return True
        return False

    def creature_hit_creature_enemy(self, target):
        board_widgets = [x for x in self.bot_gui.board_widgets]
        card_widget = GameController.find_card_by_target(target=target, widget_list=board_widgets)

        if card_widget:
            card_widget: CardWidget
            self._player_model.attack_creature_to_creature(my_creature=self.selected_creature_model,
                                                           enemy_creature=card_widget.card_logic)
            self.bot_controller.update_visual()
            self.player_controller.update_visual()
            self.selected_creature_model = False
            return True
        return False
    # endregion
