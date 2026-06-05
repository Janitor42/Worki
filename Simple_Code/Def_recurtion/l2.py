# Исполнитель преобразует число на экране.
#
# У исполнителя есть две команды, которые обозначены буквами.
#
# A.Вычти 2
#
# B.Если число кратно 3, Раздели на 3, Иначе Вычти 4
#
# Программа для исполнителя это последовательность команд.
#
# Траектория вычислений программы это последовательность результатов выполнения всех команд программы.
# Например, для программы BAB при исходном числе 99 траектория будет состоять из чисел 33, 31, 27.
#
# Сколько существует программ, которые преобразуют исходное число 36 в число 4
# и при этом траектория вычислений не содержит числа 16?


# b = 4
#
#
# def count(x):
#     print(x)
#     if x == 4:
#         return 1
#     if x < 4 or x == 16:
#         return 0
#
#     # команда A: вычесть 2
#     ways = count(x - 2)
#
#     # команда B
#     if x % 3 == 0:
#         ways += count(x // 3)
#     else:
#         ways += count(x - 4)
#     return ways

# print(count(36))


# полное решение с путями

# all_paths = []
#
#
# def count_with_path(x, target, path=None):
#     global all_paths
#     if path is None:
#         path = [x]
#
#     if x == target:
#         all_paths.append(path.copy())
#         return 1
#
#     if x < target or x == 16:
#         return 0
#
#     # Команда A: вычесть 2
#     ways = count_with_path(x - 2, target, path + [x - 2])
#
#     # Команда B
#     if x % 3 == 0:
#         ways += count_with_path(x // 3, target, path + [x // 3])
#     else:
#         ways += count_with_path(x - 4, target, path + [x - 4])
#
#     return ways
# #
# #
# # # Использование
# all_paths = []
# result = count_with_path(36, 4)
# print(f"\nВсего путей: {result}")
# print("\nВсе найденные пути:")
#
# for i, path in enumerate(all_paths, 1):
#     print(i, path)


# 24804 (Уровень: Средний)
# Герасимчук В.) Исполнитель преобразует
# число на экране. У исполнителя есть три
# команды, которые обозначены латинскими
# буквами:
# А. Умножить на 2
# В. Возвести в квадрат
# С. Возвести в куб
#
# Программа для исполнителя - это
# последовательность команд.
#
# Сколько существует программ, для которых
# при исходном числе 2 результатом является
# число 131072, при этом траектория
# вычислений не содержит одновременно 4 и
# 16?
# Траектория вычислений программы – это
# последовательность результатов
# выполнения всех команд программы.
# Например, для программы АСВ при исходном
# числе 2 траектория состоит из чисел 4, 64

# 1 вариант комбинаторика
# def rec(x, y):
#     if x == y:
#         return 1
#
#     if x > y:
#         return 0
#
#     res = rec(x * 2, y)
#     res += rec(x ** 2, y)
#     res += rec(x ** 3, y)
#
#     return res
#
#
# a = rec(2, 131072)
# b = rec(2, 4) * rec(4, 16) * rec(16, 131072)
# print(a - b)

# вариант 2 через отслеживание путей
# all_paths = []
#
#
# def rec(x, path=None):
#     if path is None:
#         path = [x]
#
#     if x == 131072:
#         all_paths.append(path.copy())
#         return 1
#
#     if x > 131072:
#         return 0
#
#     res = rec(x * 2, path + [x * 2])
#     res += rec(x ** 2, path + [x ** 2])
#     res += rec(x ** 3, path + [x ** 3])
#
#     return res
#
#
# rec(x=2)
#
# answer =[x for x in all_paths if not (4 in x and 16 in x)]
# print(len(answer))
#
# print(len(answer))
# for i in answer:
#     print(i)


def count(n, m):
    if n == m:
        return 1
    if n > m:
        return 0
    x = count(n + 2, m)
    print(x, 'a', n + 2)
    x += count(n + 3, m)
    print(x, 'b', n + 3)
    return x


print(count(n=0, m=5))
