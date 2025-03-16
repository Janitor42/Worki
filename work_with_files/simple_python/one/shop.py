import tkinter as tk
import json

# Функция для загрузки данных из JSON
def load_products():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Функция для сохранения данных в JSON
def save_products():
    with open("products.json", "w") as file:
        json.dump(products, file, indent=4)

# Функция для обновления списка товаров
def update_product_list():
    listbox_products.delete(0, tk.END)
    for idx, product in enumerate(products):
        listbox_products.insert(tk.END, f"{idx + 1}. {product['name']} - {product['price']}₽ - {product['quantity']} шт.")

# Функция для добавления нового товара
def add_product():
    name = entry_name.get()
    price = entry_price.get()
    quantity = entry_quantity.get()

    # Проверка на пустые поля и правильность данных
    if not name or not price or not quantity:
        label_status.config(text="Ошибка: Все поля должны быть заполнены!", fg="red")
        return

    try:
        price = float(price)
        quantity = int(quantity)
    except ValueError:
        label_status.config(text="Ошибка: Цена и количество должны быть числами!", fg="red")
        return

    products.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })
    save_products()
    update_product_list()

    # Очищаем поля
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    label_status.config(text="Товар успешно добавлен!", fg="green")

# Функция для удаления товара
def delete_product():
    try:
        index = int(entry_delete.get()) - 1
        if 0 <= index < len(products):
            del products[index]
            save_products()
            update_product_list()
            label_status.config(text="Товар успешно удален!", fg="green")
        else:
            label_status.config(text="Ошибка: Некорректный индекс!", fg="red")
    except ValueError:
        label_status.config(text="Ошибка: Введите корректный индекс!", fg="red")

# Функция для редактирования товара
def edit_product():
    try:
        index = int(entry_edit.get()) - 1
        if 0 <= index < len(products):
            name = entry_name.get()
            price = entry_price.get()
            quantity = entry_quantity.get()

            if not name or not price or not quantity:
                label_status.config(text="Ошибка: Все поля должны быть заполнены!", fg="red")
                return

            try:
                price = float(price)
                quantity = int(quantity)
            except ValueError:
                label_status.config(text="Ошибка: Цена и количество должны быть числами!", fg="red")
                return

            # Обновляем информацию о товаре
            products[index] = {
                "name": name,
                "price": price,
                "quantity": quantity
            }
            save_products()
            update_product_list()
            label_status.config(text="Товар успешно отредактирован!", fg="green")
        else:
            label_status.config(text="Ошибка: Некорректный индекс!", fg="red")
    except ValueError:
        label_status.config(text="Ошибка: Введите корректный индекс!", fg="red")

# Главное окно
root = tk.Tk()
root.title("Учет товаров в магазине")

# Загрузка товаров
products = load_products()

# Виджеты для добавления товара
label_name = tk.Label(root, text="Название товара:")
label_name.pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

label_price = tk.Label(root, text="Цена товара (₽):")
label_price.pack(pady=5)
entry_price = tk.Entry(root)
entry_price.pack(pady=5)

label_quantity = tk.Label(root, text="Количество товара:")
label_quantity.pack(pady=5)
entry_quantity = tk.Entry(root)
entry_quantity.pack(pady=5)

add_button = tk.Button(root, text="Добавить товар", command=add_product)
add_button.pack(pady=10)

# Виджеты для удаления товара
label_delete = tk.Label(root, text="Введите индекс товара для удаления:")
label_delete.pack(pady=5)
entry_delete = tk.Entry(root)
entry_delete.pack(pady=5)

delete_button = tk.Button(root, text="Удалить товар", command=delete_product)
delete_button.pack(pady=10)

# Виджеты для редактирования товара
label_edit = tk.Label(root, text="Введите индекс товара для редактирования:")
label_edit.pack(pady=5)
entry_edit = tk.Entry(root)
entry_edit.pack(pady=5)

edit_button = tk.Button(root, text="Редактировать товар", command=edit_product)
edit_button.pack(pady=10)

# Список всех товаров
listbox_products = tk.Listbox(root, width=50, height=10)
listbox_products.pack(pady=10)

# Статусная строка
label_status = tk.Label(root, text="", fg="black")
label_status.pack(pady=5)

# Обновление списка товаров
update_product_list()

# Запуск приложения
root.mainloop()
