import tkinter as tk

import level
import ball
import finance
import blocks


def redraw_text(all_damage):
    Screen_statistics.all_statistics.destroy_value['text'] = str(all_damage)
    Screen_statistics.all_statistics.money_value['text'] = f'{finance.Finance.money}'


class Screen_statistics:
    all_statistics = {}

    def __init__(self, win):
        self.frame_statistics = tk.Frame(win,background='red'
                                         )
        self.frame_statistics.place(x=0, y=440, width=400, height=60)

        """Menu"""
        # команда на выход меню в кнопке settings!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   нужно писать
        self.settings = tk.Button(self.frame_statistics, text='menu', height=2,
                                  relief='raised', bd=3, font=('Arial', 10))
        self.settings.grid(row=0, column=0, ipadx=5, padx=(5, 0), pady=(5, 0), rowspan=2)

        # self.frame_statistics.grid_columnconfigure(0, minsize=80)

        """Levels"""
        self.inf_level = tk.Label(self.frame_statistics, text=f' level \n{level.level}',
                                  font=('Comic San MS', 10, 'bold'))
        self.inf_level.grid(row=0, column=1, padx=(10, 0), pady=(5, 0), rowspan=2)
        self.frame_statistics.grid_columnconfigure(1, minsize=60)

        """Balls on screen"""
        self.inf_balls_on_screen = tk.Label(self.frame_statistics, text=f' Balls \n{len(ball.Ball.all_balls)}/50',
                                            font=('Comic San MS', 10, 'bold'))
        self.inf_balls_on_screen.grid(row=0, column=2, padx=(10, 0), pady=(5, 0), rowspan=2)

        """Empty"""
        # Пустая болванка для чего то если она понадобиться !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   нужно писать
        self.empty = tk.Button(self.frame_statistics, text='Empty')
        self.empty.grid(row=0, column=3, padx=(10, 0))

        """Money"""
        self.money_image = tk.Label(self.frame_statistics, text='$', font=('Comic San MS', 15, 'bold'))
        self.money_image.grid(row=0, column=4, padx=(35, 0), pady=(5, 0))

        self.money_value = tk.Label(self.frame_statistics, text=f'{finance.Finance.money}',
                                    font=('Comic San MS', 15), anchor='e')
        self.money_value.grid(row=0, column=5, pady=(5, 0), sticky='e')
        self.frame_statistics.grid_columnconfigure(5, minsize=120)

        """value destroy blocks"""
        self.destroy_image = tk.Label(self.frame_statistics, text='destroyed:', font=('Comic San MS', 10))
        self.destroy_image.grid(row=1, column=3, columnspan=2, sticky='w', padx=(10, 0))

        self.destroy_value = tk.Label(self.frame_statistics,
                                      text=f'{blocks.Block.all_damage}',
                                      font=('Comic San MS', 10))
        self.destroy_value.grid(row=1, column=5, sticky='e')

        Screen_statistics.all_statistics = self
