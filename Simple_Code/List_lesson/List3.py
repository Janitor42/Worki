import random

def Random():
    a= random.randint(100,1000)
    return str(a)

def sort_by_A_Z(inputStr):
    return inputStr[0]


name= ["Петр","Степан","Иван"]
last_name = ["Яковлев","Астахов","Иванов"]
second_name=["Иванович","Яковлевич","Александрович"]
date_of_birth=["19.01.1992", "21.2.2004","01.01.1999" ]
group=["ЭЭГ","СПГ","ААП"]


for i in range(len(last_name)):
    # id = Random()
    print(last_name[i],name[i],second_name[i],date_of_birth[i],group[i])


a=last_name.sort(key=sort_by_A_Z)
name.sort(key=a)
second_name.sort(key=a)

print()
print()

####################################################
for i in range(len(last_name)):
    # id = Random()
    print(last_name[i],name[i],second_name[i],date_of_birth[i],group[i])

