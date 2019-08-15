class Musician:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Musician name is {self.name}"

    def play(self):
        return 'play musics!!!'


class Dancer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Dancer name is {self.name}"

    def dance(self):
        return 'does dance performance'

