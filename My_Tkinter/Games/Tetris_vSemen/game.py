import tkinter as tk
from figure import Figure
from field import Field


class Game(Figure):
    # region Инициализация
    def __init__(self, win):
        super().__init__(win)

        self.speed = 4
        self.win = win
        self.game_state_flag = False

        tk.Label(self.win, text='состояние игры e', background='black', foreground='white').place(x=10, y=50)
        tk.Label(self.win, text='инфо фигуры    q', background='black', foreground='white').place(x=10, y=100)
        tk.Label(self.win, text='замена фигуры  r', background='black', foreground='white').place(x=10, y=150)

        self.game_state_text = tk.Label(self.win, text='pause', background='black', foreground='white')
        self.game_state_text.place(x=40, y=70)

        self.win.bind("<a>", self.move_left)
        self.win.bind("<d>", self.move_right)
        self.win.bind("<w>", self.rotate)

        self.win.bind('e', self.pause)
        self.win.bind('q', self.info)
        self.win.bind('r', self.restart_figure)

    # endregion

    # region Информационные методы
    def info(self, event=None):
        """Вывод информации о фигуре"""
        self.say_figure()
        print()

    # endregion

    # region Игровой цикл
    def update(self):
        """Падение фигуры"""
        if self.game_state_flag:
            if self.can_move_down():
                self.move_down()
            else:
                self.record_figure_on_field()
                Field.action_field()
                self.make_new_figure()

        self.win.after(self.speed, self.update)

    # endregion

    # region Управление игрой
    def pause(self, event=None):
        """Пауза"""
        self.game_state_flag = not self.game_state_flag
        if self.game_state_flag:
            self.game_state_text['text'] = 'run'
        else:
            self.game_state_text['text'] = 'pause'
    # endregion

    #region замена фигуры
    def restart_figure(self,event=None):
        self.make_new_figure()
    #endregion