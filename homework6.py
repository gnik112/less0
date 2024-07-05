my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002, 'Sergey': 1997}
print('Dict:', my_dict)
print('Existing value:', my_dict['Masha'])
qwery_key = 'Timofei'
print('Not existing value:', my_dict.get(qwery_key, 'Not found key "' + qwery_key + '"'))
my_dict.update({'Kamila': 1981, 'Artem': 1915})
deleted_data = my_dict.pop('Egor')
print('Deleted value:', deleted_data)
print('Modified dictionary:', my_dict)

print('')    # Просто отступ для читабельности результатов вывода

my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко', 42.314, 1, 'Яблоко', 42.314, 42.314, 1, 'Яблоко'}
print('Set:', my_set)
my_set.add(13)
my_set.add((5, 6, 1.6))
my_set.discard(1)
print('Modified set:', my_set)