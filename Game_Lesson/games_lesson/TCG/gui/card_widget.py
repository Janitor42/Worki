import tkinter as tk

from gui import config
from logic.creature_card import CreatureCard
from logic.spell_card import SpellCard


class CardWidget:
    def __init__(self, card_logic, parent_widget):
        self.stats_label = None

        self.card_logic = card_logic
        self._root = parent_widget
        self.background_color = self.get_background_color()
        self._frame = tk.Frame(self._root, bd=2, relief="solid", bg=self.background_color)
        self.price = self.card_logic.get_attr('_cost')
        self._price_view = tk.Label(self._frame, text=f'⚡{self.price}', bg=self.background_color, font=('Arial', 12, 'bold'))
        self._price_view.pack(anchor='e', pady=10)
        self.name = self.card_logic.get_attr('_name')
        self._name_view = tk.Label(self._frame, text=self.name, bg=self.background_color, font=('Arial', 10, 'bold'))
        self._name_view.pack(side='top', pady=10)
        self.define_inside_style()

    def get_price(self):
        return int(self.price)
    def get_name(self):
        return self.name

    def get_background_color(self):
        element = self.card_logic.get_attr('_element')
        if element:
            color = config.COLORS_BACKGROUND.get(element)
        else:
            color = config.COLOR_SPELL
        return color

    def define_inside_style(self):
        if isinstance(self.card_logic, CreatureCard):
            attack = self.card_logic.get_attr('_attack_power')
            health = self.card_logic.get_attr('_hp')
            self.stats_label = tk.Label(self._frame, text=f'⚔ {attack}  ❤️ {health}', bg=self.background_color,
                                        font=('Arial', 10, 'bold'))
            self.stats_label.pack(side='bottom', pady=10)

        elif isinstance(self.card_logic, SpellCard):
            type_spell = self.card_logic.get_attr('_spell_type')
            power = self.card_logic.get_attr('_power')
            ru_type = "Урон" if type_spell == "damage" else "Лечение" if type_spell == "heal" else "Щит"
            self.stats_label = tk.Label(self._frame, text=f'{ru_type}: {power}', bg=self.background_color)
            self.stats_label.pack(side='bottom', pady=10)

    def update_visual(self):
        """Метод обновляет текст характеристик, если логика карты изменилась"""
        if self.stats_label and isinstance(self.card_logic, CreatureCard):
            attack = self.card_logic.get_attr('_attack_power')
            health = self.card_logic.get_attr('_hp')
            self.stats_label.config(text=f'⚔ {attack}  ❤️ {health}')

    def place(self, x, y):
        self._frame.place(x=x, y=y, width=120, height=160)

    def destroy_widget(self):
        self._frame.destroy()

    def get_draw_obj(self):
        return [self._frame, self.stats_label, self._price_view, self._name_view]
