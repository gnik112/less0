import os.path

CLEAR_LIST = [',', '.', '=', '!', '?', ';', ':', ' - ']


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for fn in self.file_names:
            if os.path.exists(fn):
                # Загрузка данных из файла
                with open(fn, 'r', encoding='utf-8') as file:
                    fdata = file.read().lower()
                # Удаление пунктуации
                for cl in CLEAR_LIST:
                    fdata = fdata.replace(cl, '')
                # Перевод на новую строку заменить на пробел и убрать все лишнее и повторяющиеся пробелы
                all_words[fn] = ' '.join(fdata.replace('\n', ' ').strip().split()).split()
        return all_words

    def find(self, word: str):
        rez = {}
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if word.lower() == words[i]:
                    rez[name] = i + 1
                    break
        return rez

    def count(self, word: str):
        rez = {}
        for name, words in self.get_all_words().items():
            coun = 0
            for i in words:
                if word.lower() == i:
                    coun += 1
            rez[name] = coun
        return rez


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
