base = ['Ivanov paper 10', 'Petrov pens 5', 'Ivanov marker 3', 'Ivanov paper 7', 'Petrov envelope 20',
        'Ivanov envelope 5']

"""
Ivanov:
envelope 5
marker 3
paper 17
Petrov:
envelope 20
pens 5
"""
# all={}
# base=['Ivanov paper 10','Petrov pens 5','Ivanov marker 3','Ivanov paper 7','Petrov envelope 20','Ivanov envelope 5']
# for i in base:
#     word=i.split(' ')
#     if word[0] not in all:
#         all[word[0]]={word[1]:word[2]}
#     else:
#
#         all[word[0]]=[]
#
#
# for i in base:
#     word=i.split(' ')
#     if word[1] not in all[word[0]]:
#        all[word[0]].append(word[1])
#        all[word[0]].append(word[2])
#     else:
#         index=all[word[0]].index(word[1])
#         all[word[0]][index+1]=int(all[word[0]][index+1])+int(word[2])
# print(all)
#
#
#

"""2"""
ip = '145r,22-350+211.11'


print(ip)
ip_split = ip.split('.')
falsies = []


def check_symbols():
    for i in ip:
        if not i.isalnum() and i != '.':
            falsies.append(f'к символам допускается только . вы ввели {i}')


def check_len_values():
    if len(ip_split) != 4:
        falsies.append(f'длина ip должна быть 4 ряда цифр, у вас {len(ip_split)}')


# проверка что числа это числа
def check_value_is_value():
    global ip_split
    values_list = []

    for one_value in range(len(ip_split)):
        if not ip_split[one_value].isnumeric():
            falsies.append(f'число {ip_split[one_value]} вообще не число')
        else:
            values_list.append(ip_split[one_value])

    ip_split.clear()
    ip_split = values_list.copy()


# проверка на числа больше 255 или меньше 1
def check_value_max():
    for one_value in range(len(ip_split)):
        if int(ip_split[one_value]) > 255 or int(ip_split[one_value]) < 1:
            falsies.append(f'число {ip_split[one_value]} должно быть в диапазоне от 1 до 255')


check_symbols()
check_len_values()
check_value_is_value()
check_value_max()



for i in falsies:
    print(f'У вас ошибка: {i}')
