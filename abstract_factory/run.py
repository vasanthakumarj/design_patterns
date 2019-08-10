from .frog_world import FrogWorld
from .wizard_world import WizardWorld

class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()
        #print( self.hero, self.obstacle).getattr()

    def play(self):
        return self.hero.interact_with(self.obstacle)

def validate_age(name):
    try:
        age = int(input(f"Hello {name}, what's your age?"))
    except ValueError as err:
        print(f"{age} is invald. please try again...")
        return False, age
    return True, age

def main():
    name = input("Hello, what's your name?")
    valid_input = False

    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age<15 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()

if __name__ == "__main__":
    main()

