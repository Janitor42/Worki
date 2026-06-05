import tkinter as tk
import slot


class Ui:
    def __init__(self, screen):
        self.screen = screen

        self.frame = tk.Frame(self.screen, background='black', width=600, height=400)
        self.frame.place(x=100, y=50)
        self.create_slots()

        self.spin = tk.Button(self.frame, text='spin', background='green', font=('arial', 15), width=8,
                              command=self.action)
        self.spin.place(x=450, y=280)

        self.score = 100
        self.text = tk.Label(self.frame, text=f"it's your score \n {self.score}", font=('arial', 15))
        self.text.place(x=430, y=80)

        self.label_info = tk.Label(self.frame, text='there is info step', font=('arial', 12),
                                   foreground='white', background='black')
        self.label_info.place(x=430, y=150)
        self.text_entry = tk.Label(self.frame, text="your bet", font=('arial', 15), foreground='white',
                                   background='black')
        self.text_entry.place(x=0, y=330)
        self.entry = tk.Entry(self.frame, width=5, font=('arial', 20))
        self.entry.place(x=0, y=360)
        self.entry.insert(0, '1')

    def create_slots(self):
        x = 100
        y = 45

        for i in range(3):
            for q in range(3):
                slot.Slot(self.frame, x, y)
                x += 100
            x = 100
            y += 100

    def action(self):
        slot.Slot.spin_all()
        slot.Slot.check_slots()
        self.write_score()

    def write_score(self):
        count_win_slots = slot.Slot.check_score()
        raze = int(self.entry.get())
        self.score = self.score + count_win_slots * raze
        if count_win_slots * raze < 0:
            self.label_info['text'] = f'you lose {abs(count_win_slots * raze)}'
        else:
            self.label_info['text'] = f'you won {abs(count_win_slots * raze)}'
        self.text.config(text=f"it's your score \n {self.score}")
