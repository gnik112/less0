my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list_index = 0
while my_list_index < len(my_list):
    if my_list[my_list_index] > 0:
        print(my_list[my_list_index])
    elif my_list[my_list_index] < 0:
        break
    my_list_index += 1

# Если с "continue", то можно так, но код подлиннее будет:
print('') # Для читабельности результатов
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list_index = 0
while my_list_index < len(my_list):
    if my_list[my_list_index] > 0:
        print(my_list[my_list_index])
        my_list_index += 1
        continue
    if my_list[my_list_index] < 0:
        break
    my_list_index += 1

# А можно не дублировать изменение индекса, но на мой взгляд "continue" именно в этой задаче это лишнее
print('') # Для читабельности результатов
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list_index = -1
while my_list_index < len(my_list) - 1:
    my_list_index += 1
    if my_list[my_list_index] > 0:
        print(my_list[my_list_index])
        continue
    if my_list[my_list_index] < 0:
        break
