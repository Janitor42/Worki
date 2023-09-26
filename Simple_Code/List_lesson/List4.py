#создание базы данных используя массивы
last_name = ["Яковлев","Астахов","Иванов","Петров"]
name= ["Як","Александр","Иван"]
second_name=["Яковлевич","Александрович ","Иванович"]

a=[]
if len(last_name)>len(name) and len(last_name)>len(name):
    a=last_name

#Выравнивание массивов по длине
for i in range(len(a)):
   if len(last_name)>len(name):
       name.append("||")
   elif len(last_name)>len(second_name):
       second_name.append("||")

for i in range(len(a)):
    print(name[i],last_name[i],second_name[i])

# student_names=[]
#
#
# #Присваивание в массив студентов данные других массивов
# for i in range (len(last_name)):
#   a=last_name[i]+" "+name[i]+" "+second_name[i]
#   student_names.append(a)
#   print(student_names[i])