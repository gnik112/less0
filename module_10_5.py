import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


file_list = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
time1_start = datetime.datetime.now()
for file_name in file_list:
    read_info(file_name)
time1_stop = datetime.datetime.now()
print(time1_stop - time1_start)

# Многопроцессный
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        time2_start = datetime.datetime.now()
        pool.map(read_info, file_list)
    time2_stop = datetime.datetime.now()
    print(time2_stop - time2_start)
