import random

def Random_qr():
    a= random.randint(100,100000)
    return str(a)

# функция сортировки буквы от а до я
def sort_by_A_Z(inputStr):
    return inputStr[0]

def sort_by_1_99(qr):
    return str(qr)


#создание базы данных используя массивы
last_name = ["Яковлев","Астахов","Иванов"]
name= ["Як","Александр","Иван"]
second_name=["Яковлевич","Александрович ","Иванович"]
date_of_birth=["19.01.1992", "21.2 button.2004","01.01.1999" ]
group=["ЭЭГ","СПГ","ААП"]


#создание масива студентов
student_names=[]

#Присваивание в массив сутдентов данные других массивов
for i in range (len(last_name)):
    a=last_name[i]+" "+name[i]+" "+second_name[i]+" "+date_of_birth[i]+" "+ group[i]
    student_names.append(a)
    print(student_names[i])

#Сортировка массива по первой букве в Фамилии
student_names.sort(key=sort_by_A_Z)

print()

#Перебор отсортерованного массива (от а до я по фамилии)
for i in range (len(student_names)):
    print(student_names[i])

print()

qr_list=[]

#добавление персонального id к списку учеников
for i in range(len(student_names)):
    qr=Random_qr()
    student_names[i]=" personal id " ,qr, student_names[i]
    qr_list.append(qr)
    print(student_names[i])

print()

#Сортировка массива по min числу в id
student_names.sort()


for i in range(len(qr_list)):
    print(student_names[i])


print()


# создание масива групп
group_list=[]

#Присваивание в массив групп данные других массивов
for i in range(len(last_name)):
    a=group[i]+" "+last_name[i]+" "+name[i]+" "+second_name[i]+" "+date_of_birth[i]+qr[i]
    group_list.append(a)
    print(group_list[i])
print()

#Сортировка массива по первой букве в Группе
group_list.sort(key=sort_by_A_Z)

#Перебор отсортированного массива (от а до я по фамилии)
for i in range(len(group_list)):
    print(group_list[i])

