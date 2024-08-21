from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        # Задание цвета по-умолчанию
        self.set_color(0, 0, 0)
        # Задение цвета из переданных данных, если они корректны
        if (isinstance(color, tuple) or isinstance(color, list)) and len(color) == 3:
            self.set_color(color[0], color[1], color[2])
        # Сброс сторон в 1
        self.set_sides(*self.make_list_sides())
        # Задание сторон, если переданы корректные параметры
        self.set_sides(*sides)
        # Закрашенность
        self.filled = False

    def get_color(self):
        return self.__color

    def __check_cl(self, color: int):
        """Проверка одного цвета"""
        if isinstance(color, int) and color >= 0 and color <= 255:
            return True
        return False

    def __is_valid_color(self, r: int, g: int, b: int):
        """Проверка всех цветов r, g, b"""
        if self.__check_cl(r) and self.__check_cl(g) and self.__check_cl(b):
            return True
        return False

    def set_color(self, r: int, g: int, b: int):
        """Задание цветов, если цвета корректные"""
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __check_side(self, side: int):
        """Проверка одной строны"""
        if isinstance(side, int) and side > 0:
            return True
        return False

    def __is_valid_sides(self, *new_sides):
        """Проверка всех сторон"""
        if len(new_sides) == self.sides_count:
            for side in new_sides:
                if not self.__check_side(side):
                    return False
            return True
        return False

    def get_sides(self):
        """Получение всех сторон фигуры"""
        return self.__sides

    def get_side0(self):
        """Получение первой стороны фигуры"""
        if len(self.__sides) > 0:
            return self.__sides[0]
        return 0

    def __len__(self):
        """Расчет периметра как суммы длин всех сторон"""
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def make_list_sides(self, side=0):
        """Создание списка сторон указанного размера и текущего количества для фигуры"""
        if self.__check_side(side):
            return [side] * self.sides_count
        return [1] * self.sides_count


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__set_radius()

    def __set_radius(self):
        self.__radius = self.get_side0() / (2 * pi)

    def set_sides(self, *new_sides):
        """Метод переопределен, чтобы радиус менялся при изменении длины окружности"""
        super().set_sides(*new_sides)
        self.__set_radius()

    def get_square(self):
        """Возвращает площадь круга"""
        return self.__radius ** 2 * pi


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        """Расчет площади треугольника по формуле Герона"""
        # Стороны треугольника
        sides = self.get_sides()
        # Полупериметр
        p = sum(sides) / 2
        # Площадь
        s = (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        # Если передана одна сторона, то формируется куб с указанной стороной
        if len(sides) == 1:
            self.set_sides(*self.make_list_sides(sides[0]))
        # Если передано 12 сторон, то куб будет со стороной 1
        elif len(sides) == self.sides_count:
            self.set_sides(*self.make_list_sides())

    def get_volume(self):
        """Возвращает объём куба"""
        return self.get_side0() ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка изменения площади после изменения длины окружности
print(circle1.get_square())

# Проверка треугольника
triang1 = Triangle((111, 55, 31), 3, 4, 5)
print(triang1.get_square())
print(triang1.get_sides())
print(triang1.get_color())
