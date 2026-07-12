import tkinter as tk


class PlayerPanel:
    def __init__(self, root, player_logic):
        self.logic = player_logic
        self.parent = root
        self.frame_player = tk.Frame(root, width=150, height=200)

        self.frame_hand = tk.Frame(root, bg='darkgray', width=620, height=200)

        self.name_label = tk.Label(self.frame_player, text=self.logic.get_attr('_name'), font=("Arial", 20))
        self.name_label.place(x=10, y=0)

        self.hp_label = tk.Label(self.frame_player, text=f"❤ Здоровье: {self.logic.get_attr('_hp')}",
                                 font=("Arial", 12))
        self.hp_label.place(x=10, y=45)

        self.energy_label = tk.Label(self.frame_player, text=f"⚡ Энергия: {self.logic.get_attr('_energy')}/3",
                                     font=("Arial", 12))
        self.energy_label.place(x=10, y=75)

        self.hand_widgets = []

        self.clear_table_hand()

    def place_container(self, x, y):
        self.frame_player.place(x=x, y=y)
        self.frame_hand.place(x=x + 160, y=y)

    def update_visual(self):
        hp = self.logic.get_attr('_hp')
        energy = self.logic.get_attr('_energy')
        self.hp_label.config(text=f"❤ Здоровье: {hp}")
        self.energy_label.config(text=f"⚡ Энергия: {energy}/3")

    def clear_table_hand(self):
        for obj in self.hand_widgets:
            obj.destroy_widget()
        self.hand_widgets.clear()

