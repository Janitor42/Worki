import tkinter as tk
import field
import cube

# ===================== НАСТРОЙКИ ОКНА =====================
screen = tk.Tk()
screen.title("2048 Game")
screen.geometry("600x650+400+100")
screen.minsize(100, 100)
screen.maxsize(600, 600)
screen.config(background="grey")

# ===================== СОЗДАНИЕ ИГРЫ =====================
field.make_fields(screen)
cube.Cube(screen)

# ===================== ЗАПУСК =====================
screen.mainloop()