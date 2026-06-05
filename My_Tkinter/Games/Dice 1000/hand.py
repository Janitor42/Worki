from dice import Dice

import constant
from table_hand import Table_hand


class Hand:

    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.combination = {}
        self.storage = []
        self.collect_hand()

    def collect_hand(self):
        self.destroy_used_cube(for_delete=self.delete_all_storage())
        self.combination.clear()
        self.storage.clear()
        self.set_x_begin()

        for i in range(5):
            x = Dice(screen=self.screen, x=self.x, y=self.y)
            self.storage.append(x)
            self.set_x(dx=80)

    def find_red(self):
        for_delete = []
        values = []
        picture_cube = []

        for i in self.storage:
            i: Dice
            if i.get_color() == 'red':
                values.append(i.get_value())
                for_delete.append(i)
                picture_cube.append(i.get_text())
        if not values:
            return False

        if self.can_we_add_values(values=values):
            self.destroy_used_cube(for_delete=for_delete)
            Table_hand.write_dices(data=picture_cube)
            return True
        return False

    def can_we_add_values(self, values):
        old_combination = self.combination.copy()
        for i in values:
            if i in old_combination:
                old_combination[i] += 1
            else:
                old_combination[i] = 1
        score = self.find_combinations(combination=old_combination)
        if not score:
            return False
        self.combination = old_combination.copy()
        return True

    @staticmethod
    def find_combinations(combination):
        score = []
        for key, value in combination.items():
            x = 0
            if value == 5:
                x = constant.SET_COMBINATION[key] * 20
            elif value == 4:
                x = constant.SET_COMBINATION[key] * 10
            elif value == 3:
                x = constant.SET_COMBINATION[key]
            elif value == 2 and key in constant.SINGLE.keys():
                x = constant.SINGLE[key] * 2
            elif value == 1 and key in constant.SINGLE.keys():
                x = constant.SINGLE[key]

            if x == 0:
                return False
            score.append(x)

        return score

    def destroy_used_cube(self, for_delete):
        for i in for_delete:
            i.dice.destroy()
            i.rotate_cube.destroy()
            self.storage.remove(i)

    def reroll(self):
        if len(self.storage) != 0:
            for dice in self.storage:
                dice: Dice
                dice.reroll()
        else:
            print(1)
            self.collect_hand()

    def delete_all_storage(self):
        for_delete = []
        for dice in self.storage:
            for_delete.append(dice)
        return for_delete

    def set_x_begin(self, x=300):
        self.x = x

    def set_x(self, dx):
        self.x += dx
