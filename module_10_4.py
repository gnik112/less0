from threading import Thread
from random import randint
from time import sleep
import queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        self.qname = name
        super().__init__()

    def run(self):
        wtime = randint(3, 10)
        sleep(wtime)


class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            # Поиск свободного стола
            tab_guest = False
            for i in range(len(self.tables)):
                if self.tables[i].guest is None:
                    self.tables[i].guest = guest
                    self.tables[i].guest.start()
                    print(f'{self.tables[i].guest.qname} сел(-а) за стол номер {i + 1}')
                    tab_guest = True
                    break
            if not tab_guest:
                self.queue.put(guest)
                print(f'{guest.qname} в очереди')

    def discuss_guests(self):
        while True:
            # Проверка занятости столов
            tables_busy = False
            for table in self.tables:
                if table.guest != None:
                    tables_busy = True
                    break
            # Завершение обслуживания, если столы свободны и очередь пуста
            if not tables_busy and self.queue.empty():
                break
            # Проверка завершения приема пищи
            for i in range(len(self.tables)):
                if self.tables[i].guest != None:
                    if not self.tables[i].guest.is_alive():
                        print(f"{self.tables[i].guest.qname} покушал(-а) и ушёл(ушла)")
                        print(f'Стол номер {i + 1} свободен')
                        self.tables[i].guest = None
                        # Стол освободился - загрузка гостя из очереди
                        if not self.queue.empty():
                            self.tables[i].guest = self.queue.get()
                            print(f'{self.tables[i].guest.qname} вышел(-ла) из очереди и сел(-а) за стол номер {i + 1}')
                            self.tables[i].guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
