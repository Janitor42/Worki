import random
from dataclasses import dataclass

from gui.player_panel import PlayerPanel
from gui.game_field import GameField

from controller.hand_controller import HandController
from controller.ai_controller import AIController
from controller.lock_time import LockTime
from controller.lock_time import LockTime


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
        self.root = self.game_field.root
        LockTime.init(self.root)

        # self._is_player_turn = random.choice([True, False])
        self._is_player_turn = True

        self.player_controller = HandController(player_model=self._player_model, player_gui=self.player_gui)
        self.player_controller.update_visual()

        self.bot_controller = HandController(player_model=self._bot_model, player_gui=self.bot_gui)
        self.bot_controller.update_visual()

        self.ai_boot = AIController(player_model=bot_model, player_controller=self.bot_controller)

        self.game_field.end_turn_btn.config(command=self.end_turn_action)
        self.game_field.root.bind('<ButtonPress-1>', self.click)

        self.selected_card = None

        if not self._is_player_turn:
            self.game_field.root.after(1000, self.ai_turn)

    def end_turn_action(self):
        if self._is_player_turn:
            self._player_model.begin_round()
            self.player_controller.update_visual()

            self._is_player_turn = False
            self.selected_card = False

            self.game_field.turn_off_interface()
            self.game_field.root.after(1000, self.ai_turn)

    def ai_turn(self):

        card_from_hand = self.ai_boot.find_cards_from_hand()
        if card_from_hand:
            if self.ai_boot.play_card_from_hand(cards=card_from_hand):
                self.bot_controller.update_visual()
                self.game_field.root.after(1000, self.ai_turn)
                return

        card_from_table = self.ai_boot.find_card_from_board()
        if card_from_table:
            self.selected_card = card_from_table
            enemy_cards = self._player_model.get_my_table_cards()
            if not enemy_cards:
                my_widget = self.bot_controller.get_widget_by_logic(card_logic=self.selected_card)
                self.creature_hit_hero(my_widget=my_widget, enemy_frame=self.player_gui.frame_player,
                                       my_model=self._bot_model, enemy_player_model=self._player_model)
                self.player_gui.update_visual()
                self.game_field.root.after(1000, self.ai_turn)
                return
            else:
                bot_widget = self.bot_controller.get_widget_by_logic(card_logic=self.selected_card)
                choice_enemy = self.ai_boot.ai_choice_attack_creature_to_creature(enemy_cards_on_table=enemy_cards)
                enemy_widget = self.player_controller.get_widget_by_logic(card_logic=choice_enemy)
                self.creature_hit_creature(my_widget=bot_widget, enemy_widget=enemy_widget, my_model=self._bot_model,
                                           enemy_model=self._player_model, enemy_card=choice_enemy)
                print(1)
                self.game_field.root.after(1000, self.ai_turn)
                return
        #     self.player_controller.update_visual()
        #     self.bot_controller.update_visual()
        #     self.game_field.root.after(1000, self.ai_turn)
        # end
        self._bot_model.begin_round()
        self.bot_controller.update_visual()
        # self.game_field.bot_speak_end_turn_action()
        self.game_field.turn_on_interface()
        self._is_player_turn = True

    def click(self, event):
        if not self._is_player_turn:
            return
        target = event.widget
        # если атакуем вражеского героя
        if self.selected_card:
            if target in self.bot_gui.hero_widgets:
                self._is_player_turn = False
                my_widget = self.player_controller.get_widget_by_logic(card_logic=self.selected_card)
                self.creature_hit_hero(my_widget=my_widget, enemy_frame=self.bot_gui.frame_player,
                                       my_model=self._player_model, enemy_player_model=self._bot_model)
                self.bot_controller.update_visual()
                self._is_player_turn = True
                return

            # если атакуем карту героя
            enemy_card = self.bot_controller.card_form_any(target=target, atr='board_widgets')
            if enemy_card:
                self._is_player_turn = False
                my_widget = self.player_controller.get_widget_by_logic(card_logic=self.selected_card)
                bot_widget = self.bot_controller.get_widget_by_logic(card_logic=enemy_card)
                self.creature_hit_creature(my_widget=my_widget, enemy_widget=bot_widget, my_model=self._player_model,
                                           enemy_model=self._bot_model, enemy_card=enemy_card)
                self._is_player_turn = True
                return

        # если разыгрываем карту с руки
        card_from_hand = self.player_controller.card_form_any(target=target, atr='hand_widgets')
        if card_from_hand:
            self._player_model.check_card_to_play(card_logic=card_from_hand)
            self.player_controller.update_visual()
            return

        # если берем карту с доски
        card_from_board = self.player_controller.card_form_any(target=target, atr='board_widgets')
        if card_from_board:
            self.selected_card = self.player_controller.can_card_play(card=card_from_board)
            return

    def creature_hit_creature(self, my_widget, enemy_widget, my_model, enemy_model, enemy_card):

        my_hit, enemy_hit = my_model.calculate_damage_between_cards(my_creature=self.selected_card,
                                                                    enemy_creature=enemy_card)

        self.game_field.draw_info(widget=my_widget, text=f'-{enemy_hit}', x=35, y=10, time_after=2000)

        self.game_field.draw_info(widget=enemy_widget, text=f'-{my_hit}', x=35, y=10, time_after=2000)
        LockTime.wait(2)
        my_model.attack_creature_to_creature(my_creature=self.selected_card, enemy_creature=enemy_card,
                                             my_hit=my_hit, enemy_hit=enemy_hit,
                                             enemy_player_model=enemy_model)
        self.selected_card = None
        self.bot_controller.update_visual()
        self.player_controller.update_visual()
        return

    def creature_hit_hero(self, my_widget, enemy_frame, my_model, enemy_player_model):

        self.game_field.draw_info(widget=enemy_frame,
                                  text=f'-{self.selected_card.get_attack_power()}',
                                  x=75, y=10, time_after=2000)

        self.game_field.draw_info(widget=my_widget, text='бдыщь',
                                  x=35, y=10, time_after=2000)
        LockTime.wait(2)
        my_model.attack_enemy_hero(attacked_card_model=self.selected_card,
                                   enemy_player_model=enemy_player_model)
        self.selected_card = None

        return
