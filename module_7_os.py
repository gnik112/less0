import os, time

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        if os.path.exists(file):
            filepath = os.path.join(directory, file)
            filetime = os.path.getmtime(file)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(file)
            parent_dir = os.path.dirname(filepath)
            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize}'
                  f' байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
