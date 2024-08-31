import math
import time

import screen
import mouse
import ball

can = screen.can


def check_collision():
    for one_block in Block.list_blocks:

        pos_block = can.coords(one_block)
        x_1, y_1, x_2, y_2 = pos_block

        for one_ball in ball.Ball.all_ball:

            pos_ball = can.coords(one_ball)
            radius = (pos_ball[2] - pos_ball[0]) // 2
            x_center = pos_ball[0] + radius
            y_center = pos_ball[1] + radius

            nearest_x = max(x_1, min(x_center, x_2))
            nearest_y = max(y_1, min(y_center, y_2))

            distance = math.sqrt((nearest_x - x_center) ** 2 + (nearest_y - y_center) ** 2)

            if distance <= radius:
                print('collide', distance, radius,)


class Block:
    value_blocks_on_screen = 0
    list_blocks = []
    list_texts = []

    def __init__(self, x_1, y_1, x_2, y_2, protection):
        self.rectangle = can.create_rectangle(x_1, y_1, x_2, y_2,
                                              fill='DodgerBlue1',
                                              tags='block')

        Block.list_blocks.append(self.rectangle)

        x = x_2 - x_1
        y = y_2 - y_1
        x = x_1 + x // 2
        y = y_1 + y // 2

        self.value = protection
        self.text = can.create_text(x, y,
                                    text=str(self.value),
                                    font=('Times New Roman', 15),
                                    tags='block')

        Block.list_texts.append(self.text)

        self.can = can
        Block.value_blocks_on_screen += 1

        # события с мышью
        self.can.tag_bind('block', '<Button-1>', self.mouse_click_on_block)

    def __del__(self):
        Block.list_blocks.remove(self.rectangle)
        Block.list_texts.remove(self.text)

        self.can.delete(self.rectangle)
        self.can.delete(self.text)

    """Связанное с шариками"""

    def check_collision(self):
        print(self.rectangle)

    """Связанное с мышкой"""

    def check(self):
        if self.value <= 0:
            self.__del__()
            Block.value_blocks_on_screen -= 1

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
