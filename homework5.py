immutable_var = 1, "String", True, 45, 12, False
print(immutable_var)       # Вывод всего кортежа
print(immutable_var[1:3])  # Вывод элементов 1 и 2
print(immutable_var[-1])   # Вывод последнего элемента

# Изменить элемент кортежа нельзя, будет ошибка
#immutable_var[0] = 4

# Но можно изменить данные в элементе, если, например, он является списком
immutable_var = ([1, 67, True], "String", True, 45, 12, False)
print(immutable_var)
immutable_var[0][2] = "False"  # тип строка
print(immutable_var)

mutable_list = ['Иван', 'Сидоров', 34, False]
mutable_list[1] = 'Петров'                 # Изменение элемента 1
mutable_list.append('89346789365')         # Добавление элемента в конец
mutable_list.extend([234, '567', True])    # Добавление нескольких элементов
print(mutable_list)
