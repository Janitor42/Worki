# цикл for i in range
# рисование треугольников циклом используем высота треугольников ввод с клавиатуры (без вложенных циклов)
height=int(input("введите высоту треугольника"))

# #1
a=0
for i in range(1,height+1,1):
   a+=1
   print("#"*a)

# print()
#
# #2
# for i in range(1,height+1,1):
#    print("#"*a)
#    a -= 1
#
# print()

#3
# a=0
# b=height
# for i in range(1,height+1,1):
#    a+=1
#    b-=1
#    print(" "*b,"#"*a)
# a=height
# b=0
#
# print()ds
#
# #4
# for i in range(1,height+1,1):
#    print(" "*b,"#"*a)
#    a-=1
#    b+=1
#
