import tkinter as tk

all_gui = []

import ball


def create_gui_tk(balls):
    win = tk.Tk()
    win.geometry('400x800')

    for _ in balls:
        Inform(win)

    def update_gui():
        for i in all_gui:
            object_ball = ball.find_ball(i)
            i.change_inform(object_ball)
        win.after(50, update_gui)

    update_gui()

    win.mainloop()


class Inform:
    count = 0

    def __init__(self, win):
        self.win = win
        Inform.count += 1
        self.number_value = Inform.count

        self.text = tk.Label(win, text=f'Ball ({Inform.count}) Left {0} Right {0} Up {0} Down {0}')
        self.text.pack(anchor='w', side='top', expand=False)

        all_gui.append(self)

    def change_inform(self, object_ball):
        self.text.config(text=f'Ball ({object_ball.number_value}) Left {object_ball.left}'
                              f' Right {object_ball.right} '
                              f'Up {object_ball.up} '
                              f'Down {object_ball.down}')
