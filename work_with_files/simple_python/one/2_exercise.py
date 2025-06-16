# Напишите функцию create_file_with_numbers, которая принимает на вход одно целое положительное число -
# n.
#
# Функция должна создать файл с название "range_<number>.txt" и наполнить его целыми
# числами от 1 до n включительно, причем каждое число записывается  в отдельной строке
#
# Пример: функция create_file_with_numbers(5) должна создать файл range_5.txt с содержимым
#
# 1
# 2
# 3
# 4
# 5


count = 6


def create_file_with_numbers(count=count):
    file = open(f'files/from_exercise_2_{count}.txt', 'w')
    for i in range(1, count + 1):
        file.write(f'{i}\n')
    file.close()


create_file_with_numbers(count)



#счетает кол-во букв в файле (обходя \n
# file = open(f'files/from_exercise_2_6.txt', 'r')
# for i in file:
#     for q in i:
#         if q.isalnum():
#             print(q)


