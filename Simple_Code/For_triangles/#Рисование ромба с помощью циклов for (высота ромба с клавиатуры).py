#Рисование ромба с помощью циклов for (высота ромба с клавиатуры)

 #int(input())
a=int(input("Введите высоту ромба"))
h=a//2
b=h+1
x=""

for i in range(1,(h+1)+a%2,1):
    x=x+str("#")
    print(" "*(b-i)+x+"#"*i)

for i in range(1,h+1,1):
    print(" "*i+"#"*(b-i)+"#"*(b-i))
