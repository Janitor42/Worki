#Рисование равнобедренного треугольника(обратного) цикл for (высота треугольника с клавиатуры)

#int(input())

height=int(input("введите высоту треугольника"))
indent=height+1
x=""


for i in range(1,height+2,1):
   print(" "*i+"#"*(indent-i)+"#"*(indent-i))

