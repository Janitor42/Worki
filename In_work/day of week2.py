import docx
doc= docx.Document("C:/Users\Janitor\Desktop/en.docx")
all_tables = doc.tables
print('Всего таблиц в документе:', len(all_tables))

# создаем пустой словарь под данные таблиц
data_tables = {i:None for i in range(len(all_tables))}

# проходимся по таблицам
for i, table in enumerate(all_tables):
    print('\nДанные таблицы №', i)
    # создаем список строк для таблицы `i` (пока пустые)
    data_tables[i] = [[] for _ in range(len(table.rows))]
    # проходимся по строкам таблицы `i`
    for j, row in enumerate(table.rows):
        # проходимся по ячейкам таблицы `i` и строки `j`
        for cell in row.cells:
            # добавляем значение ячейки в соответствующий
            # список, созданного словаря под данные таблиц
            data_tables[i][j].append(cell.text)

    # смотрим извлеченные данные
    # (по строкам) для таблицы `i`
    print(data_tables[i])
    print('\n')
