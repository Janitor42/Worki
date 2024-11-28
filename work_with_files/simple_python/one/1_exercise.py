# Напишите функцию file_n_lines, которая печатает первые n-строка файла.
# Функция file_n_lines принимает на вход название файла и количество строк для прочтения.
#
# Не забывайте избавляться от символа переноса строки
#
# К примеру, если бы имелся файл hello.txt со следующим содержимым:
#
# h
# he
# hel
# hell
# hello

# То вызов file_n_lines(hello.txt, 3) должен распечатать следующее:
#
# h
# he
# hel


import files

file = 'files/from_exercise_1.txt'

count=3



def file_n_lines(file, count) :
    f=open(file,'r')
    for i in range(count):
        print(f.readline(),end='')
    f.close()


file_n_lines(file,count)