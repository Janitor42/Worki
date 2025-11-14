import tkinter as tk
from tkinter import ttk, messagebox


class StudentManagementSystem:

    def __init__(self, root):
        self.root = root
        self.root.title("Система управления студентами")
        self.root.geometry("600x400")

        # Основной фрейм
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Настройка весов для растягивания
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)

        # Заголовок
        title_label = ttk.Label(main_frame, text="Фильтр по имени", font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Разделительная линия
        separator1 = ttk.Separator(main_frame, orient='horizontal')
        separator1.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))

        # Кнопки управления
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))

        new_student_btn = ttk.Button(buttons_frame, text="Новый студент", command=self.add_student)
        new_student_btn.pack(side=tk.LEFT, padx=(0, 10))

        delete_student_btn = ttk.Button(buttons_frame, text="Удалить студента", command=self.delete_student)
        delete_student_btn.pack(side=tk.LEFT)

        # Разделительная линия
        separator2 = ttk.Separator(main_frame, orient='horizontal')
        separator2.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))

        # Статистика студентов
        self.student_stats = ttk.Label(main_frame, text="Студентов 0 из 0")
        self.student_stats.grid(row=4, column=0, columnspan=2, pady=(0, 10))

        # Разделительная линия
        separator3 = ttk.Separator(main_frame, orient='horizontal')
        separator3.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))

        # Статистика учителей
        self.teacher_stats = ttk.Label(main_frame, text="Учителей 0 из 0")
        self.teacher_stats.grid(row=6, column=0, columnspan=2)

        # Обновляем статистику (в реальном приложении здесь были бы реальные данные)
        self.update_statistics()

    def add_student(self):
        messagebox.showinfo("Новый студент", "Функция добавления нового студента")
        # Здесь будет логика добавления студента

    def delete_student(self):
        messagebox.showinfo("Удалить студента", "Функция удаления студента")
        # Здесь будет логика удаления студента

    def update_statistics(self):
        # В реальном приложении здесь были бы запросы к БД
        # Для демонстрации используем тестовые данные
        self.student_stats.config(text="Студентов 15 из 25")
        self.teacher_stats.config(text="Учителей 8 из 10")


def main():
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()


if __name__ == "__main__":
    main()
