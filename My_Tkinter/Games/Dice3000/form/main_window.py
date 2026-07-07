import tkinter as tk


class Main_window:

    def __init__(self):
        self.screen = tk.Tk()
        self.screen.geometry("1000x700+300+100")
        self.screen.config(background='green')

        self.screen_rules = tk.Toplevel()
        self.screen_rules.geometry('350x700+1300+100')
        self.screen_rules.config(background='black')

        self.text_rules = tk.Text(self.screen_rules, width=40, height=42)
        self.text_rules.place(x=10, y=10)
        self.read_rules()

        # Table_hand.create_table_hand(x=300, y=300, screen=self.screen)
        # Table_hand.clear_dices()

        self.player_decoration()

    def read_rules(self):
        x = open('rules.txt.txt', 'r', encoding='utf-8')
        x = x.readlines()
        for index, text in enumerate(x):
            self.text_rules.insert(f'{index}.0', text)

    def player_decoration(self):
        tk.Label(self.screen, background='DarkGreen').place(x=250, y=550, width=480, height=140)
        tk.Label(self.screen, background='DarkGreen', foreground='black', text='ваш счет',
                 font=('arial', 16), anchor='ne').place(x=850, y=550, width=120, height=140)

    def mainloop(self):
        self.screen.mainloop()
