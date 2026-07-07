import tkinter as tk

class GameBoard:
    def __init__(self, root):
        self.bot_table = tk.Frame(root, bg="gray70", width=620, height=170, bd=1, relief="sunken")
        self.bot_table.place(x=170, y=220)

        self.player_table = tk.Frame(root, bg="gray70", width=620, height=170, bd=1, relief="sunken")
        self.player_table.place(x=170, y=400)

        self.tooltip_label = tk.Label(
            root,
            text="Наведите на карту, чтобы прочитать описание",
            font=("Arial", 12, "italic"),
            bg="gray60",
            fg="white",
            wraplength=140,
            justify="center"
        )
        self.tooltip_label.place(x=10, y=300, width=150, height=150)
