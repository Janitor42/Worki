import tkinter as tk

from My_Tkinter.Games.Dice3000.form.player_form import Player_form


class Player(Player_form):

    def __init__(self, screen):
        super().__init__(screen)
        self.screen=screen
        self.do.config(command=self.action)

    # def risk(self):
    #     if not self.my_hand.storage:
    #         self.set_score()
    #         self.my_hand.collect_hand()
    #         Table_hand.clear_dices()
    #
    #     self.my_hand.reroll()
    #     self.set_state_buttons(d_state='disabled')
    #
    def action(self):
        print(1)

        # if self.my_hand.find_red():
        #     self.set_state_buttons(d_state='normal')

# def round_done(self):
#     self.set_score()
#     self.my_hand.collect_hand()
#     self.set_state_buttons(d_state='disabled')
#     Table_hand.clear_dices()
#
# def set_score(self):
#     old_score = self.score['text']
#     data = self.my_hand.find_combinations(combination=self.my_hand.combination)
#     if data:
#         round_values = sum(data)
#         self.score['text'] = old_score + round_values
#
# # def round_fall(self):
# #     self.set_state_buttons(d_state='disabled')
# #     self.my_hand.collect_hand()
#
# def set_state_buttons(self, d_state):
#     self.do['state'] = self.done['state']
#     self.done['state'] = d_state
#     self.reroll['state'] = d_state
