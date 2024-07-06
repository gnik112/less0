# Исходные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# План решения:
# 1. Сформировать список со средним баллом по оценкам
# 2. Отсортировать множество "students" с преобразованием в список
# 3. Совместить списки и преобразовать в словарь

# Средние баллы
grades_averages = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),
                   sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]),
                   sum(grades[4])/len(grades[4])]

# Сортировка students
students_sorted = sorted(students)

# Формирование результата
result_data = dict(zip(students_sorted, grades_averages))
print(result_data)