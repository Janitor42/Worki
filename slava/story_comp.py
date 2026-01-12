import tkinter as tk
from tkinter import scrolledtext


class StoryComp:
    def __init__(self, hero,callback_public_story):
        self.hero = hero
        self.callback_public_story = callback_public_story

        self.hero_name = None

        self.edit_win = tk.Toplevel()
        self.edit_win.title('рассказчик')
        self.edit_win.geometry('500x350+600+0')
        self.edit_win.config(background='gray60')



        self.lb_state_hero = tk.Label(self.edit_win, text='герой не выбрал')
        self.lb_state_hero.place(x=10, y=265)

        self.bt_choice_hero = tk.Button(self.edit_win, text='добавить персонажа', command=self.write_hero)
        self.bt_choice_hero.place(x=150, y=265)

        self.bt_write_story = tk.Button(self.edit_win, text='пиши историю', command=self.write_story)
        self.bt_write_story.place(x=300, y=265)

        self.bt_publicate = tk.Button(self.edit_win, text='слить историю', command=self.publicate_story)
        self.bt_publicate.place(x=200, y=310)
        self.setup_ui()

    def publicate_story(self):
        self.callback_public_story(text=self.text_area.get('0.0',tk.END))
        self.edit_win.destroy()

    def callback_hero(self, hero):
        self.lb_state_hero.config(text=hero)
        self.hero_name = hero


    def write_hero(self):
        self.hero(self.callback_hero)

    def write_story(self):
        self.text_story = f'{self.hero_name} просто сел и ....\n обосрался!'
        self.text_area.insert('0.0', self.text_story)

    def setup_ui(self):
        self.text_area = scrolledtext.ScrolledText(
            self.edit_win, wrap=tk.WORD, width=50, height=15
        )
        self.text_area.pack(pady=10, padx=10)
