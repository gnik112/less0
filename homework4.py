my_string = input()
print('Введена строка: "' + my_string + '", количество символов введённого текста =', len(my_string))
print('Строка в верхнем регистре:',my_string.upper())
print('Строка в нижнем регистре:',my_string.lower())
my_string = my_string.replace(' ','')
print('Первый символ строки:',my_string[0])
print('Последний символ строки:',my_string[-1])
