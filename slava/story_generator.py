from story_comp import StoryComp

import tkinter as tk
from tkinter import scrolledtext
from wizard import Wizard
from robot import  Robot


class StoryGeneratorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Генератор историй")
        self.root.geometry("500x400")
        self.state_story=None


        self.setup_ui()

    def setup_ui(self):
        # Создание текстового поля с прокруткой
        self.text_area = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, width=50, height=15
        )
        self.text_area.pack(pady=10, padx=10)

        # Создание фрейма для кнопок
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # Создание кнопок
        self.create_buttons()

    def create_buttons(self):
        # Кнопка "робот"
        self.btn_robot = tk.Button(
            self.button_frame,
            text="+робот",
            command=self.add_robot,
            width=12
        )
        self.btn_robot.grid(row=0, column=0, padx=5)

        # Кнопка "волшебник"
        self.btn_wizard = tk.Button(
            self.button_frame,
            text="+волшебник",
            command=self.add_wizard,
            width=12
        )
        self.btn_wizard.grid(row=0, column=1, padx=5)

        # Кнопка "сказка"
        self.btn_fairy_tale = tk.Button(
            self.button_frame,
            text="+сказка",
            command=self.add_fairy_tale,
            width=12
        )
        self.btn_fairy_tale.grid(row=0, column=2, padx=5)

        # Кнопка "техносказка"
        self.btn_technopunk = tk.Button(
            self.button_frame,
            text="+техносказка",
            command=self.add_technopunk,
            width=12
        )
        self.btn_technopunk.grid(row=0, column=3, padx=5)

    def add_robot(self):
        self.text_area.insert(tk.END, "Робот добавлен!\n")

    def add_wizard(self):
        self.text_area.insert(tk.END, "Волшебник добавлен!\n")

    def add_fairy_tale(self):
        StoryComp(hero=Wizard,callback_public_story=self.callback_public_story)


    def callback_public_story(self,text):
        self.text_area.insert(tk.END, text)

    def add_technopunk(self):
        StoryComp(hero=Robot,callback_public_story=self.callback_public_story)

    def mainloop(self):
        self.root.mainloop()



