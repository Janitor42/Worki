# Даны 2 списка, обрабатываем их и выводим в третий (дописать)
products= dict(Стул = 'Альфа', Стол = 'Омега', Полка = 'Гамма')
stocks=dict(Обычные_скидки=15,Высокие_скидки=30,Супер_скидка=50,Достается_в_подарок=100)

print(products["Стул"])
list1=[]
list2=[]
new_product={}
for i in products:
    list1.append(i)
for i in stocks.values():
    list2.append(i)


for i in range(len(products)):
    new_product[list1[i]]=list2[i]
print(new_product)


