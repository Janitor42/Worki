import requests
import json

import user

data = []


def create_users(shell):
    while len(data) != int(shell.quantity.get()):
        one_page(shell)

    file = open('data.json', 'w', encoding='utf-8')
    json.dump(data, file, indent=4, ensure_ascii=False)
    file.close()

    shell.clean_fields()


def one_page(shell):
    gender = choice_gender(shell)
    url = f"https://randomuser.me/api/?results={int(shell.quantity.get())}{gender}"
    response = requests.get(url).json()

    for i in response['results']:
        if len(data) == int(shell.quantity.get()):
            break
        check_age(one_object=i, age_max=int(shell.age_max.get()), age_min=int(shell.age_min.get()))


def check_age(one_object, age_min, age_max):
    age = int(one_object['dob']['age'])
    if age_max >= age >= age_min:
        data.append(one_object)


def choice_gender(shell):
    gender = shell.gender.get()

    if gender == 'любой':
        gender = ''
    elif gender == 'мужчина':
        gender = '&gender=male'
    elif gender == 'женщина':
        gender = '&gender=female'

    return gender
