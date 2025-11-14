import tkinter as tk
import random as rd


def return_slot(value):
    for obj in Slot.slots:
        if obj.number == value:
            return obj


def check_three(slot1, slot2, slot3):
    if slot1.label['text'] == slot2.label['text'] == slot3.label['text']:
        for i in (slot1, slot2, slot3):
            i.slot_win()


class Slot:
    # fruits = ["🍎", "🍌", "🍊", "🍇", "🍓", "🍍", "🥝", "🍑", "🍒", "🍉"]
    fruits = ["🍎", "🍌", "🍊", "🍇"]
    slots = []
    number = 1

    def __init__(self, frame, x, y):
        self.number = Slot.number
        self.under = tk.Label(frame, background='black', foreground='red', font=('arial', 60), text='    ')
        self.under.place(x=x - 15, y=y - 15)

        self.label = tk.Label(frame, background='white', text=rd.choice(Slot.fruits), font=('arial', 40))
        self.label.place(x=x, y=y)

        self.state = 'off'

        Slot.slots.append(self)
        Slot.number += 1

    def spin(self):
        self.label.config(text=rd.choice(Slot.fruits))
        self.under.config(background='black')
        self.state = 'off'

    def slot_win(self):
        self.under.config(background='light green')
        self.state = 'on'

    @staticmethod
    def spin_all():
        for obj in Slot.slots:
            obj.spin()

    @staticmethod
    def check_slots():
        numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [3, 6, 9], [2, 5, 8], [1, 4, 7], [1, 5, 9], [3, 5, 7]]
        for i in numbers:
            check_three(slot1=return_slot(i[0]), slot2=return_slot(i[1]), slot3=return_slot(i[2]))

    @staticmethod
    def check_score():
        count = 0
        for obj in Slot.slots:
            if obj.state in 'on':
                count += 1
        if count != 0:
            return count
        else:
            return -1
