from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        self.rname = name
        self.power = power
        self.enemy_count = 100
        self.day_count = 0
        super().__init__()

    def run(self):
        print(f'{self.rname}, на нас напали!')
        while self.enemy_count > 0:
            sleep(1)
            self.day_count += 1
            self.enemy_count -= self.power
            print(f'{self.rname} сражается {self.day_count} день(дня)..., осталось {self.enemy_count} воинов.')
        print(f'{self.rname} одержал победу спустя {self.day_count} дней(дня)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
