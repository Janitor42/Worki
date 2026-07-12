import tkinter as tk


class PlayerBoard:
        def __init__(self, root):
            self.parent = root

            # Создаем пустой фрейм для карт существ, вышедших в бой
            self.frame_table = tk.Frame(
                root,
                bg="gray70",
                width=620,
                height=170,
                bd=1,
                relief="sunken"
            )

            # Список для будущего учета виджетов карт на поле боя
            self.table_widgets = []

        def place_table(self, x, y):
            """Точечное позиционирование фрейма поля боя на экране."""
            self.frame_table.place(x=x, y=y)

        def clear_table(self):
            """Уничтожение всех виджетов карт на этом поле боя."""
            for card_widget in self.table_widgets:
                card_widget.destroy_widget()
            self.table_widgets.clear()

#TODO переписать board который универсальный для каждого как panel и работать с ним как с panel так проще