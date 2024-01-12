class Cat2:
    def __init__(self, name, age=0):
        self.name = name
        self.age=age
        print(f'Hello {self.name} my age is {self.age}')

#финализация
    def __del__(self): #вызывается перед удалением экземпляра класса автоматически
        #в нем стоит прописывать логику которая будет выполнять что то при удалении экземпляра
        print(f'удаление экземпляра {self.name}')



cat2 = Cat2('Jerry')
cat3=Cat2('lola',3)


#пока мы не нажмем 1 экземпляр cat2 будет сущесвтвовать (вывод print(если вводим 1 - в cat2 - будет лежать None
#и в этот же момент сработат __del__ в классе Cat2 для экземпляра cat2 и удалит его (смотри консоль)
while True:
    a=int(input('input 1'))
    if a==1:
        cat2=None
    print(cat2)