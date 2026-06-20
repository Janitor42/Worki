import tkinter as tk
import json


all_top_levels=[]

def create_documentation():
    file = open('data.json', 'r', encoding='utf-8')
    data = json.load(file)

    for count, obj in enumerate(data):
        User(data=obj, count=count + 1)


class User:

    def __init__(self, data, count):
        # удобный доступ
        self.number = count
        self.name = data['name']['first']
        self.surname = data['name']['last']
        self.age = data['dob']['age']
        self.gender = data['gender']
        self.nationality = data['nat']

        # Адресные данные
        self.city = data['location']['city']
        self.street = f"{data['location']['street']['name']}, {data['location']['street']['number']}"
        self.postcode = data['location']['postcode']
        self.country = data['location']['country']
        self.timezone = data['location']['timezone']['description']

        # Учетные данные
        self.email = data['email']
        self.username = data['login']['username']
        self.password = data['login']['password']

        # Дополнительные поля
        self.phone = data['phone']
        self.cell = data['cell']

        self.picture = data['picture']['large']

        self.win = tk.Toplevel()
        self.win.title(f"Досье: {self.name} {self.surname}")
        self.win.geometry("700x550")

        all_top_levels.append(self.win)
        # Настройка шрифтов
        self.title_font = ("Arial", 16, "bold")
        self.header_font = ("Arial", 12, "bold")
        self.text_font = ("Arial", 11)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.win, text=f'Досье№ {self.number}: {self.name} {self.surname}').pack(padx=10, fill=tk.X)

        # Основная информация
        self.create_section(self.win, 'Персональные данные',
                            [("ФИО", f"{self.name} {self.surname}"),
                             ("Возраст", f"{self.age} лет"),
                             ("Пол", self.gender.capitalize()),
                             ("Национальность", self.nationality)
                             ])

        # Контактная информация
        self.create_section(
            self.win,
            "Контактная информация",
            [
                ("Email", self.email),
                ("Телефон", self.phone),
                ("Мобильный", self.cell)
            ]
        )

        # Адрес
        self.create_section(
            self.win,
            "Адрес проживания",
            [
                ("Страна", self.country),
                ("Город", self.city),
                ("Улица", self.street),
                ("Почтовый индекс", self.postcode),
                ("Часовой пояс", self.timezone)
            ]
        )

        # Учетные данные
        self.create_section(
            self.win,
            "Учетные данные",
            [
                ("Логин", self.username),
                ("Пароль", self.password),
            ]
        )

    def create_section(self, parent, title, items):
        """Создает секцию с заголовком и элементами"""
        frame = tk.LabelFrame(parent, text=title)
        frame.pack(fill=tk.X, padx=5, pady=5)

        for label, value in items:
            item_frame = tk.Frame(frame)
            item_frame.pack(fill=tk.X, pady=2)

            tk.Label(
                item_frame,
                text=f"{label}:",
                font=self.header_font,
                width=20,
                anchor="e"
            ).pack(side=tk.LEFT)

            tk.Label(
                item_frame,
                text=value,
                font=self.text_font,
                anchor="w"
            ).pack(side=tk.LEFT, fill=tk.X, expand=True)
