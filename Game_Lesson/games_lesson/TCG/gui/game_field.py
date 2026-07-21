import tkinter as tk


class GameField:
    def __init__(self, parent):
        self.bot_speak_end_turn = None
        self.information_label = None
        self.root = parent
        self.end_turn_btn = tk.Button(self.root, text="Конец хода", font=("Arial", 12, "bold"), bg="lightgray")
        self.end_turn_btn.place(x=25, y=530, width=120, height=40)

    def information_action(self, text: str, x=380, y=400):
        self.information_label = tk.Label(self.root, text=text,
                                          font=("Arial", 12), bg="yellow")

        self.information_label.place(x=x, y=y)
        self.information_label.lift()
        self.information_label.after(1000, self.information_label.destroy)

    def bot_speak_end_turn_action(self):
        self.bot_speak_end_turn = tk.Label(self.root, text=f"Теперь я закончил",
                                           font=("Arial", 12), bg="yellow")

        self.bot_speak_end_turn.place(x=380, y=360)
        self.bot_speak_end_turn.lift()
        self.bot_speak_end_turn.after(1000, self.bot_speak_end_turn.destroy)

    def turn_on_interface(self):
        self.end_turn_btn.config(state='normal')

    def turn_off_interface(self):
        self.end_turn_btn.config(state='disabled')
