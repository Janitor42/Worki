# Сколько существует чисел, восьмеричная запись которых содержит 5 цифр, причем в записи нет цифры1.
# Также все цифры записи различны и никакие две чётные и две нечётные цифры не стоят рядом.

# Ответ: 180.
target = [0, 1, 2, 3, 4, 5, 6, 7]
import itertools

count = 0


def find_neighbors(i):
    if i[0] % 2 == i[1] % 2:
        return True
    if i[1] % 2 == i[2] % 2:
        return True
    if i[2] % 2 == i[3] % 2:
        return True
    if i[3] % 2 == i[4] % 2:
        return True
    return False



for i in itertools.product(target, repeat=5):
    if 0 == i[0]:
        continue
    if 1 in i:
        continue
    x = set(i)
    if len(x) != 5:
        continue
    if find_neighbors(i):
        continue

    count += 1
print(count)
