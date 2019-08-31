import abc
import urllib.request

class ResourceContent:
    def __init__(self, imp):
        self._imp = imp

    def show_content(self, path):
        self._imp.fetch(path)

class ResourceContentFetcher(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fetch(self, path):
        pass

class URLFetcher(ResourceContentFetcher):
    def fetch(self, path):
        req = urllib.request.Request(path)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                page = response.read()
                print(page)

class fileFetcher(ResourceContentFetcher):
    def fetch(self, path):
        with open(path) as finp:
            print(finp.read())


def main():
    urlfetcher = URLFetcher()
    i_face = ResourceContent(urlfetcher)
    i_face.show_content('http://python.org')

    print("==================================")

    filefetcher = fileFetcher()
    i_face = ResourceContent(filefetcher)
    i_face.show_content('file.txt')

if __name__ == '__main__':
    main()
