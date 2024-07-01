#Рисование ромба с помощью циклов for (высота ромба с клавиатуры)

 #int(input())
# a=int(input("Введите высоту ромба"))
# h=a//2
# b=h+1
# x=""
#
# for i in range(1,(h+1)+a%2,1):
#     x=x+str("#")
#     print(" "*(b-i)+x+"#"*i)
#
# for i in range(1,h+1,1):
#     print(" "*i+"#"*(b-i)+"#"*(b-i))



a=int(input("Введите высоту ромба"))
a2=a//2
a3=a//2
for i in range(1,(a//2)+(a%2)+1,1):
    print(' '*a2+'s'*i*2)
    a2-=1
for i in range(0,a//2,1):
    print(' '* (i+1)+'s'*a3*2)
    a3-=1

