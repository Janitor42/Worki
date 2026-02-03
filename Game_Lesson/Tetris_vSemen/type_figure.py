import random, tkinter as tk
import field

win = None


class Type_figure:
    PALKA = [["up"], ["up", "down"], ["down"], ["down", "down"], ]
    TROST = [["up", "down"], ["right"], ["down"], ["down", "down"]]
    GORA = [["up", "down"], ["down"], ["down", "left"], ["down", "right"]]

    def __init__(self, win):
        self.win = win
        center_block = field.Field.get_block(index=195)
        self.x = center_block.x
        self.y = center_block.y
        self.place = 195
        self.blocks = {}
        self.index = 0
        self.all_figure_index = []
        self.look = 0
        self.figure = Type_figure.TROST
        self.all_looks = [{"up": 10, "down": -10, "left": -1, "right": 1},
                          {"up": -1, "down": 1, "left": 10, "right": -10},
                          {"up": -10, "down": 10, "left": 1, "right": -1},
                          {"up": 1, "down": -1, "left": -10, "right": 10}]
        print(len(self.all_looks))
        self.place_figure(self.figure)
        self.fall()

    def place_figure(self, figure):
        self.get_index(figure)
        for i in range(len(figure)):
            index = self.all_figure_index[i]
            x = field.Field.get_block(index=index).get_x()
            y = field.Field.get_block(index=index).get_y()
            block = tk.Label(win, text=f"", background="yellow", foreground="green",
                             font=("Arial", 13), height=1,
                             width=2)
            block.place(x=x, y=y)
            self.blocks[block] = (x, y)

    def get_index(self, figure):
        index = self.place
        for i in range(len(figure)):
            index = self.place
            i_figure = figure[i]
            for look in i_figure:
                index += self.all_looks[self.look][look]
            self.all_figure_index.append(index)

    def check_wall(self, num):
        for key, value in self.blocks.items():
            block = self.blocks[key]
            if block[0] == num:
                return True

    def replace_place(self, num):
        for key, value in self.blocks.items():
            a = value
            self.blocks[key] = (value[0] + num, value[1])

    def hide_figures(self):
        for key, value in self.blocks.items():
            key.place_forget()

    def place_figures(self, figure):
        for i, block in enumerate(self.blocks):
            index = self.place
            i_figure = figure[i]
            for g in i_figure:
                index += self.all_looks[self.look][g]
            x = field.Field.get_block(index=index).get_x()
            y = field.Field.get_block(index=index).get_y()
            block.place(x=x, y=y)

    def get_all_x(self):
        return [x[0] for x in self.blocks.values()]

    def move_left(self):
        if self.check_wall(num=120):
            return
        self.hide_figures()
        self.place -= 1
        self.replace_place(num=-26)
        self.place_figures(figure=self.figure)

    def move_right(self):
        if self.check_wall(num=354):
            return
        self.hide_figures()
        self.place += 1
        self.replace_place(num=26)
        self.place_figures(figure=self.figure)

    def rotate(self):
        result = self.all_looks[self.index]
        self.index = (self.index + 1) % len(self.all_looks)
        self.look += 1
        if self.look == 4:
            self.look = 0
        self.hide_figures()
        self.place_figures(figure=self.figure)
        return result

    def fall_it(self):
        for i in self.all_figure_index:
            print(i)
            field.Field.edit_block(index=i)
            self.hide_figures()
            self.figure=random.choice([Type_figure.TROST,Type_figure.PALKA,Type_figure.GORA])
            self.place_figures(figure=self.figure)
    def fall(self):
        self.place += -10
        for i in self.all_figure_index:
            a = i - 10
            if a < 0:
                self.fall_it()
                return
        self.get_index(self.figure)
        self.get_index(figure=self.figure)
        self.hide_figures()
        self.place_figures(figure=self.figure)
        self.win.after(100, self.fall)
