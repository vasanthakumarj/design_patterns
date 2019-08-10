class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f"{self} encounters {obstacle} and action is {act}"
        print(msg)


class Bug:
    def __str__(self):
        print('a bug')

    def action(self):
        return 'eats it!!!'

#FrogWorld is factory
class FrogWorld:
    def __init__(self, name):
        print(name)
        self.player_name = name

    def __str__(self):
        print("\n\n\t==========Frog world============")

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()