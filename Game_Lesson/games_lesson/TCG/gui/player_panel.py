import tkinter as tk


class PlayerPanel:
    def __init__(self, root, player_logic):
        self.logic = player_logic
        self.parent = root
        self.frame_player = tk.Frame(root, width=150, height=200)

        self.frame_hand = tk.Frame(root, bg='darkgray', width=620, height=200)
        self.frame_board = tk.Frame(root, bg="gray70", width=620, height=200, bd=1, relief="sunken")
        self.name_label = tk.Label(self.frame_player, text=self.logic.get_attr('_name'), font=("Arial", 20))
        self.name_label.place(x=10, y=0)
        self.hp_label = tk.Label(self.frame_player, text=f"❤ Здоровье: {self.logic.get_attr('_hp')}",
                                 font=("Arial", 12))
        self.hp_label.place(x=10, y=45)

        self.energy_label = tk.Label(self.frame_player, text=f"⚡ Энергия: {self.logic.get_attr('_energy')}/3",
                                     font=("Arial", 12))
        self.energy_label.place(x=10, y=75)

        self.sing_label = tk.Label(self.frame_player,background='black')
        self.sing_label.place(x=10, y=100, width=130, height=90)

        self.hand_widgets = []
        self.board_widgets = []

    def place_container(self, x, y_hand, y_board):
        self.frame_player.place(x=x, y=y_hand)
        self.frame_hand.place(x=x + 160, y=y_hand)
        self.frame_board.place(x=x + 160, y=y_board)

    def update_visual(self):
        hp = self.logic.get_attr('_hp')
        energy = self.logic.get_attr('_energy')
        self.hp_label.config(text=f"❤ Здоровье: {hp}")
        self.energy_label.config(text=f"⚡ Энергия: {energy}/3")

    def clear_widgets(self, atr):
        atr = getattr(self, atr, [])
        for obj in atr:
            obj.destroy_widget()
        atr.clear()


    def get_draw_obj(self):
        return [self.frame_player, self.name_label, self.hp_label, self.energy_label, self.sing_label]