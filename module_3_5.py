
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    # Также будет логичным пропустить нули в конце числа, например - 4020300
    # Из-за "отложенной оценки" в проверке and - ошибки не будет
    if len(str_number) > 1 and int(str_number[1:]) > 0:
        return first * get_multiplied_digits(int(str_number[1:]))
    return first

result = get_multiplied_digits(40203)
print(result)

result = get_multiplied_digits(40203000)
print(result)
