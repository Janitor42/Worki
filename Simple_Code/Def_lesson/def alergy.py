def is_allergen(product):
    if product=="апельсин" or product=="арахис" or product=="мед":
        return False
    else:
        return True

product = input('Введите название продукта')

if is_allergen(product)==False:
    print('Есть вероятность аллергической реакции')
else:
    print('Продукт безопасен')