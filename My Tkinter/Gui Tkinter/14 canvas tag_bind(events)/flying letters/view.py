import tkinter as tk
import model

win = tk.Tk()
x = '800'
y = '800'
win.geometry(x + 'x' + y)
win.config(background='black')

can = tk.Canvas(bg='white', width=int(x) - 50, height=int(y) - 100)
can.pack(anchor='s', pady=10)

views = []

win.update()


class View:
    views=[]
    def __init__(self, master_model):
        self.letter = can.create_text(master_model.x, master_model.y,
                                      text=master_model.text, fill='purple',
                                      font=('Arial', 25), activefill='brown')



        View.views.append(self)
    def move(self, master_model):
        can.coords(self.letter, master_model.x, master_model.y)


def add_views():
    if len(model.letters) > 0 and len(model.letters) > len(views):
        views.append(View(model.letters[-1]))


def move_all():
    for i in range(len(views)):
        views[i].move(model.letters[i])


def draw():
    add_views()
    move_all()
    # win.update()
