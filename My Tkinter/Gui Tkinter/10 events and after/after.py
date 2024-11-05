import tkinter as tk

# Настройка функции обновления метки
def update_label():
    global counter
    counter += 1  # Увеличиваем счетчик на 1
    label.config(text=f"Count: {counter}")  # Обновляем текст метки

    # Запланировать следующий вызов этой функции через 1000 миллисекунд (1 секунду)
    root.after(1000, update_label)


# Создаем главное окно
root = tk.Tk()
root.title("Tkinter after Example")

# Счетчик
counter = 0

# Создаем метку
label = tk.Label(root, text="Count: 0", font=("Arial", 24))
label.pack(pady=20)

# Начинаем обновление метки
update_label()

# Запускаем главный цикл приложения
root.mainloop()