# установка библиотеки (из коробки нам ее не дали)\
import requests
import json
from pprint import pprint

# requests.get(url) — получение данных
# requests.post(url, data) — отправка данных (например, форма)
# requests.put(url, data) — обновление ресурса
# requests.delete(url) — удаление ресурса
# requests.head(url) — получение заголовков
# requests.patch(url, data) — частичное обновление


# get()!!!!!!!
# https://randomuser.me/
# url = 'https://randomuser.me/api'  # переменная в которую записываем уру ссылку api
# response = requests.get(url)  # погружаем в requests с параметром get()
# response = response.json()  # подучаем и сохраняем ответ в json()
# pprint(response)  # отформатированный принт

# дальше будет делать это короче для в 1 строку
# pprint(requests.get('https://randomuser.me/api').json())

# документация на randomuser:
# https://randomuser.me/documentation

# "https://randomuser.me/api/" - базовый ulr (случайный пользователь весь)
# pprint(requests.get('https://randomuser.me/api').json())

# "https://randomuser.me/api/?results=5" (несколько пользователей за раз)
# url = "https://randomuser.me/api/?results=5"
# pprint(requests.get(url).json())
# получили json с 5 человеками

# "https://randomuser.me/api/?gender=female&results=3" -(получить пользователя по полу female or male + сразу несколько)
# url = "https://randomuser.me/api/?gender=female&results=3"
# pprint(requests.get(url).json())
# получили json с 3 человеками все они female ! обратите внимание что в url докидываем &result=3 так можно делать

# https://randomuser.me/api/?nat=ru - (национальность)
# url = "https://randomuser.me/api/?nat=ru&gender=female&results=2"
# pprint(requests.get(url).json())
# получили json с 2 человеками все они female национальность rus и так же их 2 потому что results=2

# https://randomuser.me/api/?seed=abc123&results=2 (seed - уникальный номер который мы можем использовать что бы попадать
# на одних и тех же сгенерированных пользователей а не новые рандомы)
# url='https://randomuser.me/api/?seed=aaa&results=2'
# for i in range(3):
#     pprint(requests.get(url).json())
#     print('-'*120)
# получили 3 раза одних и тех же персонажей потому что использовали seed

# https://randomuser.me/api/?inc=name,email,gender (возвращает только определенные поля - экономит время и меньше данных)
# url = 'https://randomuser.me/api/?inc=name,email,gender'
# pprint(requests.get(url).json())
# получили только выбранные поля ниже пример одного и того же пользователя с inc и без
# pprint(requests.get('https://randomuser.me/api/?inc=name,email,gender&seed=aaa&results=2').json())
# print('-'*120)
# pprint(requests.get('https://randomuser.me/api/?&seed=aaa&results=2').json())

# https://randomuser.me/api/?exc=login,registered - (исключать поля опять же экономия и простота)
# url='https://randomuser.me/api/?exc=login,registered,location'
# pprint(requests.get(url).json())
# выключил нам поля которые мы указали в exc через запятую

# https://randomuser.me/api/?seed=test&results=5&page=1 пагинация ( работает только с seed - это верь конкретный список,
# и нужна что бы загружать список меньшими частями не за раз выгружать 100 пользователей а сделать 10 загрузок по 10 человек,
# для работы с большими данными необходима)
# for i in range(1, 4):
#     url = f'https://randomuser.me/api/?seed=bbb&inc=name,gender&results=2&page={i}'
#     pprint(requests.get(url).json())
# из за того что используем пагинацию получаем список частями из за того что используем seed это один и тот же набор
# пользователей из за того что используем inc - получаем только имена и пол этих пользователей
