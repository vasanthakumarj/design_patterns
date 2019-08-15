from external import Dancer, Musician

class Club:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the club {self.name}'

    def organize_event(self):
        return 'hires an artist to perform for the people'

class Adaptor:
    def __init__(self, obj, adopted_methods):
        self.obj = obj
        self.__dict__.update(adopted_methods)

    def __str__(self):
        return str(self.obj)

def main():
    objects = [Club('Jazz Cafe'), Musician('Roy Ayers'), Dancer('Shane sparks')]

    for obj in objects:
        if hasattr(obj, 'play') or hasattr(obj, 'dance'):
            if hasattr(obj, 'play'):
                adopted_methods = dict(organize_event=obj.play)
            elif hasattr(obj, 'dance'):
                adopted_methods = dict(organize_event=obj.dance)

            #referencing adaptor object here
            obj = Adaptor(obj, adopted_methods)

        print(f'{obj} {obj.organize_event()}')


if __name__ == '__main__':
    main()
