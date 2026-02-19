import tkinter as tk
import field
import figure

win = tk.Tk()
win.title("Tetris")
win.geometry("500x700+740+250")
win.minsize(200, 200)
win.maxsize(1000, 1000)
win.config(background="black")

field.Field.make_field(win=win)

figure.Figure(win)

win.mainloop()
