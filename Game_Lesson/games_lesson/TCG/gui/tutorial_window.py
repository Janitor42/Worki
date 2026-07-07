import tkinter as tk
from tkinter import messagebox


class TutorialWindow:
    """Класс окна обучения. Работает через композицию на стандартных цветах tkinter."""

    def __init__(self, root,path):
        # 1. Создаем независимое окно верхнего уровня
        self.path = path
        self.window = tk.Toplevel(root)
        self.window.title("Руководство мага: Правила игры")
        self.window.geometry("500x600+900+200")
        self.window.resizable(False, False)

        # 2. Делаем окно модальным (блокируем клики по главной игре)
        self.window.grab_set()

        # Используем простые стандартные цвета, понятные ученикам
        self.bg_color = "gray"  # Стандартный серый фон
        self.text_bg = "white"  # Белый фон для текста rules.txt.txt
        self.text_color = "black"  # Черный цвет шрифта
        self.btn_bg = "lightgray"  # Светло-серый цвет для кнопки

        self.window.configure(bg=self.bg_color)

        # 3. Строим интерфейс
        self._create_widgets()

        # 4. Загружаем правила из файла
        self._load_rules()

    def _create_widgets(self):
        """Создание и упаковка элементов интерфейса на базовых виджетах."""
        # Простой текстовый заголовок
        title_label = tk.Label(
            self.window,
            text="Книга Правил Стихий",
            font=("Arial", 16, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        title_label.pack(pady=15)

        # Контейнер для текста и скроллбара
        text_frame = tk.Frame(self.window, bg=self.bg_color)
        text_frame.pack(expand=True, fill="both", padx=20, pady=5)

        # Самый обычный вертикальный скроллбар
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side="right", fill="y")

        # Текстовое поле
        self.text_area = tk.Text(
            text_frame,
            wrap="word",
            yscrollcommand=scrollbar.set,
            font=("Arial", 11),
            bg=self.text_bg,
            fg=self.text_color,
            padx=15,
            pady=15,
            bd=1,
            relief="solid"
        )
        self.text_area.pack(side="left", expand=True, fill="both")

        # Связываем скроллбар и текстовое поле
        scrollbar.config(command=self.text_area.yview)

        # Кнопка закрытия
        # Внутри метода _create_widgets измените кнопку закрытия:
        close_button = tk.Button(
            self.window,
            text="Всё понятно, закрыть книгу",
            font=("Arial", 11, "bold"),
            bg=self.btn_bg,
            fg=self.text_color,
            bd=1,
            relief="raised",
            padx=20,
            pady=8,
            command=self._on_close ) # Перенаправляем на безопасный метод закрытия

        close_button.pack(pady=20)

        # И добавьте этот новый метод в самый низ класса TutorialWindow:
    def _on_close(self):
        """Безопасное закрытие окна с возвратом фокуса главной игре."""
        self.window.grab_release()  # Освобождаем перехват ввода

        # Получаем ссылку на главное окно и возвращаем ему фокус
        parent = self.window.master
        if parent:
            parent.focus_set()

        self.window.destroy()  # И только теперь уничтожаем окно правил

    def _load_rules(self):
        """Чтение внешнего файла и безопасная вставка текста."""
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                content = file.read()

            # Разрешаем запись, вставляем текст и блокируем от изменений
            self.text_area.config(state="normal")
            self.text_area.insert("1.0", content)
            self.text_area.config(state="disabled")

        except FileNotFoundError:
            messagebox.showerror(
                "Ошибка",
                "Файл 'data/rules.txt.txt' не найден!\nПожалуйста, проверьте папку проекта."
            )
            self.window.destroy()
