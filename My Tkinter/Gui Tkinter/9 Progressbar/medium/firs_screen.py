import tkinter as tk
import second_screen

all_el = []
screen = None


def page_two():
    for i in all_el:
        i.destroy()
    all_el.clear()
    second_screen.create_page_two(screen)


def create_page_one(screen):
    label1 = tk.Label(screen, text='Здравствуйте',
                      font=('Helvetica', 20), background='white',
                      )

    label2 = tk.Label(screen, text='Нажмите "Начать установку" ',
                      font=('Helvetica', 18), background='white',
                      )

    label1.pack(pady=(200, 0))
    label2.pack()

    button_start = tk.Button(screen, text='Начать установку', border=2,
                             command=page_two)
    button_start.pack(padx=(200, 0), pady=(100, 0))

    all_el.append(label1)
    all_el.append(label2)
    all_el.append(button_start)
