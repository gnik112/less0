from time import sleep


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return str(self.nickname)


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        """ Вход пользователя при совпадении логина и пароля """
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user

    def register(self, nickname, password, age):
        """ Регистрация нового пользователя """
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        self.current_user = User(nickname, password, age)
        self.users.append(self.current_user)

    def log_out(self):
        self.current_user = None

    def add(self, *Videos):
        """ Добавление нового видео"""
        for vd in Videos:
            if isinstance(vd, Video):
                add_true = True
                for i in self.videos:
                    if i.title == vd.title:
                        add_true = False
                        break
                if add_true:
                    new_video = Video(vd.title, vd.duration, vd.time_now, vd.adult_mode)
                    self.videos.append(new_video)

    def get_videos(self, sear_word):
        _list = []
        for vd in self.videos:
            if vd.title.lower().find(sear_word.lower()) >= 0:
                _list.append(vd.title)
        return _list

    def watch_video(self, title):
        # Проверка авторизации пользователя
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        # Поиск видео
        for vd in self.videos:
            if vd.title == title:
                # Проверка возраста пользователя
                if vd.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                # Воспроизведение видео
                for vd.time_now in range(vd.duration):
                    print(str(vd.time_now + 1), end=' ')
                    sleep(0.5)
                vd.time_now = 0
                print("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
