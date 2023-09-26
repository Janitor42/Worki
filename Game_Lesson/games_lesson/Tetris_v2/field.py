from wrap import sprite


class Field():
    def __init__(self):
        self.fields = []
        self.work_fields = []
        self.work_fields_copy = []
        self.len_row = {}
        self.remove_element = None
        self.remove_elements=[]
        self.height_field = 21
        self.width_field = 11

        self._create_field()

    def _create_field(self):

        y_y = 590
        x_x = 20
        numbers = 1
        height = 1
        for y in range(self.height_field):
            for x in range(self.width_field):
                dici = {'x': x_x, 'y': y_y, 'state': False, 'number': numbers, 'height': height}
                x_x += 30
                self.fields.append(dici)
                numbers += 1
                x += 200
            y_y -= 30
            x_x = 20
            height += 1

    def rewrite_and_work_fields(self, check):
        if check:
            self._record_field()
            self._add_row()

    def _record_field(self):
        for i in self.fields:
            if i['state']:
                name = sprite.add('pacman', i['x'], i['y'])
                sprite.set_size(name, 28, 28)
                dici = {'name': name, 'height': i['height']}
                self.work_fields.append(dici)
                i['state'] = False

    def _add_row(self):
        self.len_row.clear()
        for i in self.work_fields:
            if i['height'] not in self.len_row:
                self.len_row[i['height']] = 1
            else:
                self.len_row[i['height']] += 1
        self._check_row_in_ten()

    def _check_row_in_ten(self):
        self.remove_elements.clear()
        a = 0
        for i in self.len_row.items():
            if i[1] == 10:
                self.remove_element = i
                self.remove_elements.append(self.remove_element[0])
                self._destroy_row()
                a += 1
        for i in range(a):
            self._move_other_row()

    def _move_other_row(self, ):
        self.remove_elements.sort()
        for i in self.work_fields:
            if i['height'] > self.remove_elements[0]:
                sprite.move(i['name'], 0, 30)
                i['height'] = i['height'] - 1

    def _destroy_row(self):
        self.work_fields_copy.clear()
        for i in self.work_fields:
            if i['height'] == self.remove_element[0]:
                sprite.hide(i['name'])
                sprite.remove(i['name'])
            else:
                self.work_fields_copy.append(i)

        self.work_fields.clear()
        self.work_fields += self.work_fields_copy

    def add_field(self, figure):
        if not figure.check:
            return
        for dot in self.fields:
            if collide_dot(dot, figure.names):
                dot['state'] = True


def collide_dot(dot, names):
    for name in names:
        if sprite.is_collide_point(name, dot['x'], dot['y']):
            return True
    return False
