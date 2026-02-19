import tkinter as tk
import random

from field import Field

free_colours = ["red"]
numbers = [2, 4]


class Cube:
    my_cube = None

    def __init__(self, screen):
        self.screen = screen

        self.speed_game = 1

        self.cube_place_on_desk = -2
        self.x = 246
        self.y = 0
        self.state = "ready"

        self.cube = tk.Label(self.screen, width=7, height=3, background='red', text=random.choice(numbers),
                             font=('arial', 13))
        self.cube.place(x=self.x, y=self.y)

        for key in ["<d>", "<D>", "<Right>"]:
            self.screen.bind(key, self.move_cube_right)
        for key in ["<a>", "<A>", "<Left>"]:
            self.screen.bind(key, self.move_cube_left)
        for key in ["<space>", "<Return>", "<KP_Enter>", "<Down>"]:
            self.screen.bind(key, self.set_state)

        self.screen.after(self.speed_game, self.game())
        Cube.my_cube = self

    def destroy_cube(self):
        self.cube.destroy()
        Cube.my_cube = None

    def create_new_cube(self):
        Field.rewrite_place(obj_cube=self)
        self.destroy_cube()
        Cube(screen=self.screen)

    """move left and right"""

    # region
    def move_cube_right(self, event=None):
        if self.x < 392 and self.state == "ready":
            self.cube_place_on_desk += 1
            self.set_x(x=73)
            self.cube.place(x=self.x, y=self.y)

    def move_cube_left(self, event=None):

        if self.x > 100 and self.state == "ready":
            self.cube_place_on_desk -= 1
            self.set_x(x=-73)
            self.cube.place(x=self.x, y=self.y)

    # endregion

    """get methods"""

    # region

    def get_state(self):
        return self.state

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_pos(self):
        return [self.x, self.y]

    def get_cube_place_on_desk(self):
        return self.cube_place_on_desk

    # endregion

    """set methods"""

    # region
    def set_state(self, event=None):
        if self.state == 'ready':
            self.state = 'move'

        if self.state == 'finish':
            self.state = 'ready'

    def set_y(self):
        self.y += 1

    def set_x(self, x):
        self.x += x

    def change_cube_param(self, obj_field):
        self.cube_place_on_desk = obj_field.get_number_on_desk()

    def move_cube(self):
        self.set_y()
        self.cube.place(x=self.x, y=self.y)

    # endregion

    """move_down"""

    # region

    def find_who_under_you(self):
        place_cube_now = self.cube_place_on_desk

        if place_cube_now >= 26:
            return True

        next_place_cube = place_cube_now + 5
        place_down = Field.find_place_down(next_place_cube=next_place_cube)
        place_down: Field

        if place_down.get_state() != 'open':
            return True

        if place_down.get_pos() == self.get_pos():
            self.change_cube_param(obj_field=place_down)

        return False

    # endregion

    """check the working squares"""

    # region

    def run_squares(self):
        while True:
            Field.collapse = False

            Field.connect_all_play_squares()
            Field.fall_all_play_squares()

            if not Field.collapse:
                break

    # endregion

    """game logic"""

    # region

    def game(self, event=None):
        if self.get_state() == 'move':
            if self.find_who_under_you():
                self.create_new_cube()
                self.run_squares()
                return

            self.move_cube()

        self.screen.after(self.speed_game, self.game)

    # endregion
