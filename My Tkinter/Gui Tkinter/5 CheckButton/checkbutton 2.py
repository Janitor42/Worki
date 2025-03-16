import tkinter as tk
from tkinter import ttk


def update_total():
    """Пересчитывает итоговую сумму в зависимости от выбранных опций."""
    total = base_price
    details = []
    if delivery_var.get():
        total += 200
        details.append("Доставка")
    if gift_wrap_var.get():
        total += 150
        details.append("Подарочная упаковка")
    if express_var.get():
        total += 300
        details.append("Срочная обработка")
    if insurance_var.get():
        total += 250
        details.append("Страхование посылки")
    if vip_service_var.get():
        total += 500
        details.append("VIP-обслуживание")

    total_label.config(text=f"Итоговая сумма: {total} руб.")
    details_label.config(text="Выбрано: " + ", ".join(details) if details else "Вы ничего не выбрали")


def toggle_vip():
    """Если выбрано VIP-обслуживание, отключает другие опции."""
    if vip_service_var.get():
        delivery_var.set(0)
        gift_wrap_var.set(0)
        express_var.set(0)
        insurance_var.set(0)
    update_total()


def reset_options():
    """Сбрасывает все выбранные опции."""
    delivery_var.set(0)
    gift_wrap_var.set(0)
    express_var.set(0)
    insurance_var.set(0)
    vip_service_var.set(0)
    update_total()


# Основное окно
root = tk.Tk()
root.title("Калькулятор заказа")
root.geometry("350x300")

# Базовая цена заказа
base_price = 500

# Заголовок
title_label = ttk.Label(root, text="Выберите дополнительные услуги:", font=("Arial", 12))
title_label.pack(pady=10)

# Переменные для Checkbutton
delivery_var = tk.IntVar()
gift_wrap_var = tk.IntVar()
express_var = tk.IntVar()
insurance_var = tk.IntVar()
vip_service_var = tk.IntVar()

# Фрейм для опций
frame = ttk.LabelFrame(root, text="Дополнительные опции")
frame.pack(pady=5, padx=10, fill="both")

# Checkbuttons
chk_delivery = ttk.Checkbutton(frame, text="Доставка (+200 руб.)", variable=delivery_var, command=update_total)
chk_delivery.pack(anchor="w", padx=10)

chk_gift_wrap = ttk.Checkbutton(frame, text="Подарочная упаковка (+150 руб.)", variable=gift_wrap_var,
                                command=update_total)
chk_gift_wrap.pack(anchor="w", padx=10)

chk_express = ttk.Checkbutton(frame, text="Срочная обработка (+300 руб.)", variable=express_var, command=update_total)
chk_express.pack(anchor="w", padx=10)

chk_insurance = ttk.Checkbutton(frame, text="Страхование посылки (+250 руб.)", variable=insurance_var,
                                command=update_total)
chk_insurance.pack(anchor="w", padx=10)

chk_vip_service = ttk.Checkbutton(frame, text="VIP-обслуживание (+500 руб.)", variable=vip_service_var,
                                  command=toggle_vip)
chk_vip_service.pack(anchor="w", padx=10)

# Итоговая сумма
total_label = ttk.Label(root, text=f"Итоговая сумма: {base_price} руб.", font=("Arial", 12, "bold"))
total_label.pack(pady=10)

details_label = ttk.Label(root, text="Вы ничего не выбрали", font=("Arial", 10))
details_label.pack()

# Кнопка сброса
reset_button = ttk.Button(root, text="Сбросить", command=reset_options)
reset_button.pack(pady=5)

# Запуск основного цикла Tkinter
root.mainloop()
