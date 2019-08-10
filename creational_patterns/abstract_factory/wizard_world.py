class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f" encounters {obstacle} and action is {act}"
        return(msg)


class ork:
    def __str__(self):
        print('an evil')

    def action(self):
        return 'kills it!!!'

#WizardWorld is factory
class WizardWorld:
    def __init__(self, name):
        self.player_name = name

    def __str__(self):
        return("\n\n\t==========Wizard world============")

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return ork()