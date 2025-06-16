from faker import Faker

# Создаем объект Faker (с русским языком)
fake = Faker('ru_RU')

# Генерируем фейковые данные
name = fake.name()  # Фейковое имя
address = fake.address()  # Фейковый адрес
email = fake.email()  # Фейковый email
text = fake.text()  # Фейковый текст

# Выводим результаты
print(f"Имя: {name}")
print(f"Адрес: {address}")
print(f"Email: {email}")
print(f"Текст: {text}")