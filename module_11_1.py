import requests
from PIL import Image, ImageOps
import numpy as np

# Библиотека requests
print('Библиотека requests')

# получения параметров
try:
    response = requests.options('https://google.com', timeout=2)
    print(response.headers)
except:
    print('Ошибка')

# получение данных методом get
try:
    response = requests.get('https://api.github.com')
    if response.status_code == 200:
        print('Ответ успешно получен, данные:')
        print(response.text)
    elif response.status_code == 404:
        print('Страница не найдена')
except:
    print('Ошибка')

# запрос данных методом post
try:
    PostParams = {'param1': 'value1', 'param2': 'value2'}
    response = requests.post('https://httpbin.org/post', PostParams, timeout=2)
    print(response.json()['form'])
except:
    print('Ошибка')

# Библиотека pillow
print()
print('Библиотека pillow')

imj = Image.open("01.jpg")
# Вывод параметров картинки
print(f'Формат: {imj.format}, Размер: {imj.size}, Режим: {imj.mode}')
# Показать картину (запустится программа просмотра изображений)
imj.show()
# Поворот изображения на 90 градусов
imj01 = imj.rotate(90)
# Запись картинки в новый файл
imj01.save('02.jpg')
# Изменеие размера картинки
imj02 = imj.resize((128, 128))
# Запись картинки в новый файл
imj02.save('03.jpg')
# Создание черно-белой картинки с оттенками серого
imj_grey = ImageOps.grayscale(imj)
imj_grey.save('04.jpg')

# Библиотека numpy
print()
print('Библиотека numpy')

# Создание массива со случайными значениями
arr = np.random.randint(0, 10, size=(2, 3))
# Количество измерений массива
print(f'Создан массив, количество измерений массива: {arr.ndim}')
print(arr)
# Количество строк и столбцов
print(f'Строк и столбцов: {arr.shape}')
# Возведение в квадрат каждого элемента
print('Возведение в квадрат каждого элемента:')
print(arr ** 2)
# Можно просто создать массив
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print('Создан еще один массив:')
print(arr2)
print('сложение массивов:')
print(arr + arr2)
