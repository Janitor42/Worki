# Приветствие: Напишите lambda-функцию, которая принимает имя (строку) и возвращает строку
# "Привет, [имя]!".
# a=lambda x:f'hello {x}'
# print(a(x='petr'))

# Удвоитель: Напишите lambda-функцию,
# которая принимает число и возвращает его удвоенное значение.
# a=lambda x:x**2
# print(a(x=3))

# Проверка на чётность: Напишите lambda-функцию, которая принимает число и возвращает True,
# если оно чётное, и False — если нет.
# a=lambda x:True if x%2==0 else False
# print(a(x=3),a(x=4))

# Сумма трёх: Напишите lambda-функцию,
# которая принимает три числа и возвращает их сумму.
# a=lambda x,y,z:x+y+z
# print(a(4,4,4))

# Кратность: Напишите lambda-функцию,
# которая принимает два числа a и b и возвращает True,
# если a делится на b без остатка.
# z = lambda a, b: True if a % b == 0 else False
# print(z(a=10,b=6))

# Уровень 2: Работа со встроенными функциями (map, filter, sorted)
numbers = [1, 2, 3, 4, 5]
words = ["яблоко", "дом", "компьютер", "но"]
# Квадраты: Используя map и lambda, создайте новый список,
# содержащий квадраты элементов исходного списка чисел.
# a=map(lambda x:x**2,numbers)
# print(list(a))

# Только чётные: Используя filter и lambda, отфильтруйте список чисел, оставив только чётные.
# a=filter(lambda x:x%2==0,numbers)
# print(list(a))

# Длина слов: Используя map и lambda, создайте список длин слов из списка строк.
# a=map(lambda x:len(str(x)),words)
# print(list(a))

# Короткие слова:
# Используя filter и lambda, отфильтруйте список слов, оставив только те, длина которых меньше 4 символов.
# a=filter(lambda x: True if len(str(x))<4 else False,words)
# print(list(a))

# Сортировка по длине: Используя sorted и lambda,
# отсортируйте список слов по их длине (от самого короткого к самому длинному).
# a=sorted(words,key=lambda x:len(str(x)))
# print(list(a))

# Сортировка по последнему символу: Используя sorted и lambda, отсортируйте список слов по последней букве каждого слова.
# a=sorted(words,key=lambda x:str(x[-1]))
# print(list(a))


# Уровень 3: Комбинированные и более сложные задачи
# Степень числа: Напишите lambda-функцию, которая принимает число x и возвращает другую функцию.
# Возвращаемая функция должна принимать число n и возвращать x в степени n.
# Подсказка: lambda x: lambda n: ...
#
# a=lambda x:lambda n:x**n
# print(a(3)(5))

# Сортировка сложных структур: Дан список кортежей: people = [("Анна", 25), ("Петр", 20), ("Мария", 30)].
# Отсортируйте его:
# По возрасту (второй элемент).
# По длине имени (первый элемент).

# people = [("Анна", 25), ("Петр", 20), ("Мария", 30)]
# a=sorted(people,key=lambda x:x[1])
# print(list(a))
# b=sorted(people,key=lambda x:len(str(x)),reverse=True)
# print(list(b))

# Обработка пар элементов: Даны два списка a = [1, 2, 3] и b = [4, 5, 6].
# Используя map и lambda, создайте список, где каждый элемент — это сумма элементов a и b на соответствующих позициях.
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# x=map(lambda x,y:x+y,a,b)
# print(list(x))


text = 'In the hole in the ground there lived a hobbit'
first=text.find('h')
reversed_str=''.join(reversed(text))
last=reversed_str.find('h')
last=len(text)-last
new_text = text[:first] + text[first:last+1].replace('h', 'H') + text[last+1:]
print(new_text)


elves = {
    "Бобби": ("машинки", 5),
    "Джесси": ("куклы", 4),
    "Фредди": ("конструкторы", 6),
    "Элли": ("мягкие игрушки", 3),
    "Гномик": ("пазлы", 7),
    "Снежинка": ("настольные игры", 4),
    "Искорка": ("книги", 5)
}
order = {
    "машинки": 50,
    "куклы": 40,
    "конструкторы": 60,
    "мягкие игрушки": 30,
    "пазлы": 70,
    "настольные игры": 35,
    "книги": 45
}
work_hours_per_day = 8
days_until_christmas = 7
total_time = {}

for i in elves:
    key = elves[i][0]
    all_toys = order[key]

    power_elf_in_hour = elves[i][1]

    all_hours = all_toys // power_elf_in_hour

    all_minutes = all_toys % power_elf_in_hour

    if all_minutes != 0:
        toy_in_minute = 60 / power_elf_in_hour
        all_minutes = int(all_minutes * toy_in_minute)
    else:
        all_minutes = 0

    total_time[i] = (all_hours, all_minutes)

print("Общее время для каждого эльфа:")
for key, minutes in total_time.items():
    print(f"Эльф {key} {minutes[0]} часов {minutes[1]} минут")



