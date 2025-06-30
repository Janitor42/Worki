import requests
import json
from pprint import pprint


# 1
# Задание : Сортировка пользователей по полу
# Напиши программу, которая:
# Получит список пользователей с параметром gender.
# Отсортирует пользователей по полу (женщины и мужчины) и выведет их отдельно.
# Условия:
# Используй параметр gender в запросе.
# Напечатай список мужчин и женщин по очереди (например, сначала все мужчины, потом все женщины
# (имя город, страна, дата рождения, username).

# url = 'https://randomuser.me/api/?results=6'
# save = requests.get(url).json()
#
# for i in save['results']:
#     if i['gender'] == 'female':
#         print(f" Name :{i['name']['first']}\n City :{i['location']['city']}\n Country :{i['location']['country']}\n"
#               f" Date of birth : {i['dob']['date']}\n Username: {i['login']['username']}\n {'-' * 120}")
# print('xx'*80)
# for i in save['results']:
#     if i['gender'] == 'male':
#         print(f" Name :{i['name']['first']}\n City :{i['location']['city']}\n Country :{i['location']['country']}\n"
#               f" Date of birth : {i['dob']['date']}\n Username: {i['login']['username']}\n {'-' * 120}")

# 2
# Задание: Создание генератора пользователей с пагинацией
# Напиши скрипт, который будет получать пользователей с API randomuser.me, используя пагинацию и выводить имена и emails.
# Убедись, что пагинация работает: ты должен загрузить несколько страниц, а не просто одну.
# Условия:
# Используй параметр page.
# Выведи только имена и emails.
# Добавь проверку на ошибку, если запрос не успешен (например, код ошибки 404 или 500).

# for i in range(1, 6):
#     try:
#         url = f'https://randomuser.me/api/?seed=aaa&results=4&page={i}'
#         response=requests.get(url)
#         response.raise_for_status() #проверка статуса
#         response=response.json()
#         response=response['results']
#         for user in response:
#             print(f" Name :{user['name']['first']} , Email : {user['email']}")
#         print('_'*120)
#     except Exception as e:
#         print('ошибка')


# 3
# Задание: Пагинация с множественными запросами
# Напиши функцию, которая будет:
# Принимать два параметра: results (количество пользователей на странице) и
# total_users (общее количество пользователей, которых нужно получить).
# Функция должна делать несколько запросов для получения всех пользователей. Используй пагинацию (page).
# Все полученные пользователи должны быть сохранены в список и распечатаны.


# all_users = []
# results = 5
# total_users = 16
# def go(results, total_users):
#     page=1
#     while True:
#         url = f'https://randomuser.me/api/?seed=test&results={results}&page={page}'
#         resp = requests.get(url)
#         resp.raise_for_status()  # проверка статуса
#         resp = resp.json()
#         resp = resp['results']
#         for user in resp:
#             if len(all_users) >= total_users:
#                 return
#             all_users.append(user)
#         page+=1
#
# go(results, total_users)
# for i in all_users:
#     pprint(i)
#     print('--'*100)


# более сложные задачи:
# Задание — Анализ: сколько пользователей из каких стран
# Цель: Получить, например, 50 пользователей и вывести:
# Сколько человек из каждой страны (country).
# Отсортировать по убыванию.

# all_users = {}
# results = 5
# total_users = 50
#
#
# def go(results, total_users):
#     page = 1
#     value=1
#     while True:
#         try:
#             url = f'https://randomuser.me/api/?seed=test&results={results}&page={page}'
#             resp = requests.get(url)
#             resp.raise_for_status()  # проверка статуса
#             resp = resp.json()
#             resp = resp['results']
#             for user in resp:
#                 if value > total_users:
#                     return
#                 if user['location']['country'] not in all_users:
#                     all_users[user['location']['country']] = 1
#                 else:
#                     all_users[user['location']['country']] += 1
#                 value+=1
#             page += 1
#         except:
#             print('page not opening, start next page')
#
#
# go(results, total_users)
#
# all_users_sorted = dict(sorted(all_users.items(), key=lambda item: item[1], reverse=True))
#
# for q, w in all_users_sorted.items():
#     print(q, w)
