import tkinter as tk
import ui

screen = tk.Tk()
screen.geometry('800x500')
screen.config(background='DarkSeaGreen')


my_app = ui.Ui(screen)


screen.mainloop()