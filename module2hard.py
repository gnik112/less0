def get_cod(num):
    cod = ''
    for int1 in range(1, num // 2 + 1):
        for int2 in range(int1 + 1, num):
            if num % (int1 + int2) == 0:
                cod += f'{int1}{int2}'
    return cod

for i in range(3, 21):
    print(f'{i} - ' + get_cod(i))
