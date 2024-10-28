import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode: bool = False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user
            else:
                print("Пользователь не найден")

    def register(self, nickname, password, age):
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print("Такой пользователь уже существует")
                return
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video_1 in args:
            if video_1 not in self.videos:
                self.videos.append(video_1)

    def get_videos(self, text):
        list_videos = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_videos.append(video.title)
        return list_videos

    def watch_video(self, video_1):
        if not self.current_user:
            print("Войдите в аккаунт")
            return

        for i in self.videos:
            if i.title == video_1:
                if i.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18, просмотр запрещен")
                return

        for y in range(i.duration):
            print(y, end = " ")
            i.time_now += 1
        i.time_now = 0
        print("Конец видео")

if __name__ == "__main__":
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