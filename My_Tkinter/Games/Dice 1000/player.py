import tkinter as tk

from hand import Hand
from table_hand import Table_hand


class Player:

    def __init__(self, screen, x=300, y=600):
        self.screen = screen
        self.x = x
        self.y = y
        self.my_hand = Hand(screen=self.screen, x=self.x, y=self.y)

        self.score = tk.Label(self.screen, text=0, font=('arial', 20), background='darkgreen', anchor='e')
        self.score.place(x=890, y=580, width=80)

        self.description_move = tk.Text(self.screen, background='green',
                                        width=14, height=10, relief="flat",
                                        bd=0, highlightthickness=0, font=('arial', 12))
        self.description_move.place(x=880, y=300)

        self.reroll = tk.Button(self.screen, text='Переброс', font=('arial', 14), command=self.risk,
                                width=10, anchor='e', state='disabled')
        self.reroll.place(x=730, y=572)

        self.do = tk.Button(self.screen, text="Отложить ", font=('arial', 14), command=self.action, width=10,
                            anchor='e')
        self.do.place(x=730, y=611)
        self.done = tk.Button(self.screen, text='Я пас', font=('arial', 14), command=self.round_done
                              , width=10, anchor='e', state='disabled')
        self.done.place(x=730, y=650)

        # self.round_over = tk.Button(self.screen, text='Вариантов нет', font=('arial', 14),
        #                             )
        # self.round_over.place(x=730, y=550)

    def risk(self):
        if not self.my_hand.storage:
            self.set_score()
            self.my_hand.collect_hand()
            Table_hand.clear_dices()

        self.my_hand.reroll()
        self.set_state_buttons(d_state='disabled')

    def action(self):
        if self.my_hand.find_red():
            self.set_state_buttons(d_state='normal')

    def round_done(self):
        self.set_score()
        self.my_hand.collect_hand()
        self.set_state_buttons(d_state='disabled')
        Table_hand.clear_dices()

    def set_score(self):
        old_score = self.score['text']
        data = self.my_hand.find_combinations(combination=self.my_hand.combination)
        if data:
            round_values = sum(data)
            self.score['text'] = old_score + round_values

    # def round_fall(self):
    #     self.set_state_buttons(d_state='disabled')
    #     self.my_hand.collect_hand()

    def set_state_buttons(self, d_state):
        self.do['state'] = self.done['state']
        self.done['state'] = d_state
        self.reroll['state'] = d_state
