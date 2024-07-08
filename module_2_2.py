first, second, third = int(input('Введите число 1: ')), int(input('Введите число 2: ')), int(input('Введите число 3: '))
if first == second == third:   # if first == second and second == third:  - Можно так
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')
