import tkinter as tk


class Player_form:

    def __init__(self, screen, x=300, y=600):
        self.screen = screen
        self.x = x
        self.y = y
        # self.my_hand = Hand(screen=self.screen, x=self.x, y=self.y)

        self.score = tk.Label(self.screen, text=0, font=('arial', 20), background='darkgreen', anchor='e')
        self.score.place(x=890, y=580, width=80)

        self.description_move = tk.Text(self.screen, background='green',
                                        width=14, height=10, relief="flat",
                                        bd=0, highlightthickness=0, font=('arial', 12))
        self.description_move.place(x=880, y=300)

        self.reroll = tk.Button(self.screen, text='Переброс', font=('arial', 14),
                                width=10, anchor='e', state='disabled')
        self.reroll.place(x=730, y=572)

        self.do = tk.Button(self.screen, text="Отложить ", font=('arial', 14), width=10,
                            anchor='e')
        self.do.place(x=730, y=611)
        self.done = tk.Button(self.screen, text='Я пас', font=('arial', 14)
                              , width=10, anchor='e', state='disabled')
        self.done.place(x=730, y=650)

        self.round_over = tk.Button(self.screen, text='Вариантов нет', font=('arial', 14),
                                    )
        self.round_over.place(x=730, y=550)
