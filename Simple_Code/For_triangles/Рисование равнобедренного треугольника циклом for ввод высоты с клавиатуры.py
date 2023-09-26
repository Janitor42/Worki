
#Рисование равнобедренного треугольника цикл for (высота треугольника с клавиатуры)

#int(input())

height=int(input("введите высоту треугольника"))
indent=height+1
x=""

for i in range(1,height+1,1):
   x=x+str("#")
   print(" "*(indent-i)+x+"#"*i)