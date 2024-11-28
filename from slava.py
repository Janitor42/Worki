
#1
# lst=[1,1,1,1]
# print(*lst)
#
# diki={'sep':'===','end':'___'}
# print(1,2,3,**diki)




# * - распаковка для списка множества строка
# ** - распаковка словаря



#кваргс keywordarguments(параметры превращаются в словарь(затем с ним действия(строчка 19))
def aa (a,b,c=1,**kwargs):
    print(kwargs['d'])
    print(a,b,c,kwargs)

aa(a=100,b=100,d=3,z=10)




#2

def tief(original):
    def part(*args,**kwargs):
        print(args,kwargs)
        original(*args,**kwargs)
    return part

@tief
def add(a, b):
    c = a + b
    print(c)



def bbb(a,b):
    c=a-b
    print(c)

bbb=tief(bbb)

add(1,2)