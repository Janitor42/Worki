#
import pygame# импорт pygame

window= pygame.display.set_mode((400,400)) #Создание дисплея игры
pygame.display.set_caption("Hello") #Создание заголовка игры

screen=pygame.Surface((40,40)) #Создание обьекта в игре на дисплее

done=True # Переменная для окончания работы окна Pygame

#Цикл игры в котором происходят события
while done:
    # Цикл который проверяет наличия события (нажатие на крестик) если нажатие произошло то выход из while
    # Соответственно остановка программы
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            done=False

    screen.fill((5,250,220)) #Закрашиваем обьект screen в цвет (палитра RGB)

    window.blit(screen,(10,70))# Позиция обьекта screen на экране (x and y)

    pygame.display.flip() # Обновление экрана


