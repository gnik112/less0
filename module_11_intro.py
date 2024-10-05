import sys, pprint


def introspection_info(obj):
    rez = {}
    # Тип объекта
    rez['type'] = type(obj)
    # Атрибуты объекта
    rez['attributes'] = dir(obj)
    # Методы объекта
    rez['methods'] = [x for x in dir(obj) if callable(getattr(obj, x))]
    # Название модуля
    rez['module'] = __name__
    # ОС на которой запущено
    rez['platform'] = sys.platform
    return rez


number_info = introspection_info(42)
print(number_info)

print()
print('Более читаемо:')
pprint.pprint(number_info)


class Test:
    def __init__(self, a1, a2):
        self.attr_1 = a1
        self.attr_2 = a2

    def main_method(self):
        return


class_obj = Test(0, 'Test')

class_info = introspection_info(class_obj)

print()
print('Информация по классу:')
pprint.pprint(class_info)
