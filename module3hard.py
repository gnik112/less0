
def calculate_structure_sum(data):
    if isinstance(data, str):
        return len(data)
    if isinstance(data, int) or isinstance(data, float):
        return data
    if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
        summa = 0
        for i in data:
            summa += calculate_structure_sum(i)
        return summa
    if isinstance(data, dict):
        summa = 0
        for key, value in data.items():
            summa += calculate_structure_sum(key) + calculate_structure_sum(value)
        return summa
    # Неописанные выше или неизвестные типы данных не будут учитываться в общей сумме
    return 0

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
