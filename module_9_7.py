def is_prime(func):
    def wrapper(a, b, c):
        rez = func(a, b, c)
        # Проверка числа - простое или нет
        prost = True
        for i in range(2, (rez // 2) + 1):
            if rez % i == 0:
                prost = False
                break
        if prost:
            print("Простое")
        else:
            print("Составное")
        return rez
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
