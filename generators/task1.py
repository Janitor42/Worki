# Задача 1: Генератор квадратов
# Создайте генератор, который будет генерировать квадраты чисел от 1 до n.

# def gener(n):
#     for i in range(n):
#         yield i**2
#
# gen=gener(5)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# Задача 2: Генератор чётных чисел
# Создайте генератор, который будет генерировать все чётные числа в заданном диапазоне от start до end.

# def even_value(start,finish):
#     if start % 2 != 0:
#         start += 1
#     for i in range(start, finish + 1, 2):  # Используем шаг 2
#         yield i
# gen=even_value(10,30)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# Задача 3: Генератор букв заданного диапазона
# Создайте генератор, который будет генерировать все заглавные буквы английского алфавита
# в диапазоне от A до заданной буквы.

# from string import ascii_uppercase
#
#
# def gener(finish_letter):
#     finish_letter = finish_letter.upper()
#     all_letters = list(ascii_uppercase)
#     for i in all_letters:
#         yield i
#         if finish_letter == i:
#             break
#
#
# gen = gener('c')
# print(next(gen))
# print(next(gen))
# print(next(gen))


# Задача 4: Генератор повторяющихся символов
# Создайте генератор, который будет принимать строку и генерировать её символы с их индексами.

# def gen_str(st):
#     for sym in range(len(st)):
#         yield sym,st[sym]
#
# gen=gen_str('корова')
#
#
# for item in gen:
#     print(item)


# Задача 5: Генератор элементов из двух списков
# Напишите генератор, который будет чередовать элементы из двух переданных списков до тех пор,
# пока не исчерпаются элементы обоих списков.


# def double_gen(lst_a,lst_b):
#     max_len=max(len(lst_a),len(lst_b))
#     for i in range(max_len):
#         if len(lst_a) > i:
#             yield lst_a[i]
#         if len(lst_b)>i:
#             yield  lst_b[i]
#
#
# gen=double_gen([4,4,4,4,4,4],['hi'])
#
# for i in gen:
#     print(i)




