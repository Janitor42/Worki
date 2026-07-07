import tkinter as tk

from gui import config
from logic.creature_card import CreatureCard
from logic.spell_card import SpellCard


class CardWidget:
    def __init__(self, cart_logic, parent):
        self.card_logic = cart_logic
        self._root = parent
        self.background_color = self.get_background_color()
        self._frame = tk.Frame(self._root, bd=2, relief="solid", bg=self.background_color)

        self.stats_label = None
        self.define_inside_style()

    def get_background_color(self):
        element = self.card_logic.get_attr('_element')
        if element:
            color = config.COLORS_BACKGROUND.get(element)
        else:
            color = config.COLOR_SPELL
        return color

    def define_inside_style(self):
        price = self.card_logic.get_attr('_cost')
        tk.Label(self._frame, text=f'⚡{price}', bg=self.background_color, font=('Arial', 12, 'bold')).pack(anchor='e',
                                                                                                           pady=10)

        name = self.card_logic.get_attr('_name')
        tk.Label(self._frame, text=name, bg=self.background_color,font=('Arial',10,'bold')).pack(side='top', pady=10)

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
        self._frame.place(x=x, y=y, width=100, height=150)
