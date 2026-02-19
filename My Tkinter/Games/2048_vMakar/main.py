import tkinter as tk
import field
import figure

screen = tk.Tk()
screen.title("class lesson")
screen.geometry("600x650+400+100")
screen.minsize(100, 100)
screen.maxsize(600, 600)
screen.config(background="grey")

field.make_fields(screen)
figure.Cube(screen)


screen.mainloop()

