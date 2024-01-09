from wrap import sprite as sp
import figure


class Star(figure.Figure):
    def __init__(self, x, y, size, number):
        super().__init__(x, y, size)
        self.number = number
        self.live = True

        self.name = sp.add('mario-items', self.x, self.y, 'star')
        self.name_number = sp.add_text(str(self.number), self.x, self.y, text_color=(255, 255, 255), bold=True,
                                       back_color=(0, 0, 0))
        sp.set_width_proportionally(self.name, self.size)

    def light_star(self):
        if self.size < 60:
            self.size += 1
            sp.set_width_proportionally(self.name, self.size)
        else:
            self.size = 20

    def del_obj_star(self):
        sp.remove(self.name)
        sp.remove(self.name_number)
