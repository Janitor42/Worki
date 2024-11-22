import random as rd
import string as st

letters = []


def add_letter(can):
    letters.append(Letter(can))


class Letter:
    def __init__(self, can):
        self.text = rd.choice(st.ascii_lowercase)
        self.x = rd.randint(0, 780)
        self.y = rd.randint(0, 780)
        self.speed_x = 2
        self.speed_y = 2

        self.name = can.create_text(self.x, self.y,
                                    text=self.text, font=('Arial', 25,'bold'),)

    def step(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y

    def side(self):
        if self.x > 750:
            self.speed_x = -2
        if self.x < 0:
            self.speed_x = 2
        if self.y > 750:
            self.speed_y = -2
        if self.y < 0:
            self.speed_y = 2


def move_all(can):
    for i in letters:
        i.step()
        i.side()
        can.move(i.name, i.speed_x, i.speed_y)
