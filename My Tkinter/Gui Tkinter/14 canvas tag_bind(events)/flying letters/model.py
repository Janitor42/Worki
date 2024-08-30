import random as rd
import string as st


def add_letters():
    letters.append(Letter())


class Letter:
    def __init__(self):
        self.text = rd.choice(st.ascii_lowercase)
        self.x = rd.randint(0, 780)
        self.y = rd.randint(0, 780)
        # self.rotate = rd.randint(1, 15)
        self.speed_x = 2
        self.speed_y = 2

    def step(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y


def move_all():
    for i in letters:
        i.step()
        print(i.x, i.y)


letters = []
letters.append(Letter())
