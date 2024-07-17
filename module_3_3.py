
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(34)
print_params(56, 78)
print_params('Hello', 'world', '!')
print()

print_params(b = 25)
print_params(c = [1,2,3])
print()

values_list = [1, 'строка', True]
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)
print()

values_list_2 = [45, False]
print_params(*values_list_2, 42)
print()

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)