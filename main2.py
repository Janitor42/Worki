import tkinter as tk


class GameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tag Bind Example in Tkinter")
        self.canvas = tk.Canvas(master, width=400, height=400, bg='white')
        self.canvas.pack()

        # Создаем квадрат и круг с тегами
        self.square = self.canvas.create_rectangle(50, 50, 150, 150, fill='blue', tags='shape')
        self.circle = self.canvas.create_oval(200, 50, 300, 150, fill='red', tags='shape')

        # Привязываем событие клика к элементам с тегом 'shape'
        self.canvas.tag_bind('shape', '<Button-1>', self.on_shape_click)

    def on_shape_click(self, event):
        # Получаем все идентификаторы объектов под курсором
        overlapping_items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)

        for item in overlapping_items:
            # Если это круг, изменяем его цвет
            if item == self.circle:
                self.canvas.itemconfig(self.circle, fill='green')
                print("Круг был щелкнут!")
            # Если это квадрат, изменяем его цвет
            elif item == self.square:
                self.canvas.itemconfig(self.square, fill='yellow')
                print("Квадрат был щелкнут!")


if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()