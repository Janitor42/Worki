

#__setattr__ (self,key,value)-атоматически при изменении значения класса
#можем запретить создавать какой то определенный именной атрибут (бросать исключение)
# __setattr__(self,key,value):
#     if key=='z':
#         raise ValueError('недопустимое имя атрибута')
#     else:
#         object.__setattr__(self,key,value)


#__getattribute__(self,item)-автоматически при получении свойст класса с именем item
#может понадобиться для запрещения на прямую к значению атрибута
# __getattribute__(self,item)
#     if item =='x':
#         raise ValueError ('доступ запрещен')
#     else:
#         return object.__getattribute__(self,item)



#__getattr__(self,item)-автоматически при получении несуществующего свойства item класса
#можем использовать что бы не получить исключение когда обращаемся к несуществующему методу экземпляра
# __getattr__(self,item)
#     return False

#delattr__(self,item)-автоматически при удалении свойства
#Может понадобиться для удаления определенного поля в экземпляре самого класса а не в классе
# __delattr__(self,item)
# object.__delattr__(self,item)

