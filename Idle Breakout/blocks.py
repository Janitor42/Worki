import random as rd

import screen
import mouse

can = screen.can


def dici_trye():
    print(len(Block.all))


class Block:
    all_blocks = 0
    all = []

    def __init__(self, x_1, y_1, x_2, y_2, protection):
        self.rectangle = can.create_rectangle(x_1, y_1, x_2, y_2,
                                              fill='DodgerBlue1',
                                              tags='block')
        self.all.append(self.rectangle)

        x = x_2 - x_1
        y = y_2 - y_1

        self.value = protection
        self.text = can.create_text(x_1 + x // 2, y_1 + y // 2,
                                    text=str(self.value),
                                    font=('Times New Roman', 15),
                                    tags='block')

        self.all.append(self.text)

        self.can = can

        # события с мышью
        self.can.tag_bind('block', '<Button-1>', self.mouse_click_on_block)
        Block.all_blocks += 1

    def __del__(self):
        self.all.remove(self.rectangle)
        self.all.remove(self.text)

        self.can.delete(self.rectangle)
        self.can.delete(self.text)

    """Связанное с шариками"""

    def touch_to_ball(self):
        pass

    """Связанное с мышкой"""

    def check(self):
        if self.value <= 0:
            self.__del__()
            Block.all_blocks -= 1

    def mouse_click_on_block(self, even):
        name = self.can.find_closest(even.x, even.y)

        name = name[0]
        if name % 2 != 0:
            self.rectangle = name
            self.text = name + 1

            self.can.itemconfigure(self.rectangle, fill='red')
            self.can.itemconfigure(self.text, text=self.subtract_from_block_on_click())
            self.check()

        elif name % 2 == 0:
            self.text = name
            self.rectangle = name - 1

            self.can.itemconfigure(self.rectangle, fill='red')
            self.can.itemconfigure(self.text, text=self.subtract_from_block_on_click())
            self.check()

    def subtract_from_block_on_click(self):
        self.value = int(self.can.itemcget(self.text, 'text')) - mouse.Mouse.power
        self.can.itemconfigure(self.text, text=str(self.value))
