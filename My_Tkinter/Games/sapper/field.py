import tkinter as tk
import random as rd


class Field:

    def __init__(self, can):
        self.can = can

        self.number = 1
        self.rows = 10
        self.column = 10

        self.mines = 10

        self.x = 10
        self.y = 10

        self.figures = []
        self.pos_figures = []

        self.id_mines = []

        for i in range(self.rows):
            for q in range(self.column):
                self.rec = self.can.create_rectangle(
                    self.x, self.y, self.x + 40, self.y + 40,
                    fill='white', tag='open')

                self.figures.append(self.rec)
                self.pos_figures.append([self.x + 15, self.y + 15])

                self.number += 1
                self.x += 40

                self.can.tag_bind(self.rec, '<Button-1>', self.say)

            self.x = 10
            self.y += 40

        count = 0
        while count < self.mines:
            id_bomb = rd.randint(0, self.rows * self.column)
            if id_bomb not in self.id_mines:
                self.id_mines.append(id_bomb)
                count += 1
        print(self.id_mines)

    def say(self, event):
        # Получаем текущие координаты клика
        x, y = event.x, event.y
        # касание
        for i in self.figures:
            coords = self.can.coords(i)  # Получаем координаты прямоугольника
            if coords[0] <= x <= coords[2] and coords[1] <= y <= coords[3]:
                if self.check_places_bomb(i):
                    pass
                else:
                    self.another_check(coord_x=coords[0], coord_y=coords[1], i=i)

    def check_places_bomb(self, i):
        if i in self.id_mines:
            self.can.itemconfig(i, fill='red')
            return True

    def another_check(self, coord_x, coord_y, i):
        count = 0
        discovered = []
        for x in range(-40, 80, 40):
            for y in range(-40, 80, 40):
                closest = self.can.find_closest(x + coord_x, y + coord_y)
                closest = list(closest)[0]
                if closest in self.id_mines and closest not in discovered:
                    count += 1
                    discovered.append(closest)
                    print(discovered)

        if count > 0:
            self.can.itemconfig(i, fill='orange')
            self.can.create_text(
                coord_x + 20, coord_y + 20, text=count, font=('Arial', 10, 'bold'))
        else:
            self.can.itemconfig(i, fill='green')
            self.can.create_text(
                coord_x + 20, coord_y + 20, text=count, font=('Arial', 10, 'bold'))
