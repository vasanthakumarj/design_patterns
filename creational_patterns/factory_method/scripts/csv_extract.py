import csv

class CsvDataExtractor():
    def __init__(self, file_path):
        with open(file_path, 'r') as finp:
            self.data = csv.reader(finp)

    @property
    def parsed_data(self):
        for movie in self.data:
            print(f"Title: {movie['title']}")
            year = movie['year']
            if year:
                print(f"Year: {year}")
            director = movie['director']
            if director:
                print(f"Director: {director}")
            genre = movie['genre']
            if genre:
                print(f"Genre: {genre}")
            print()

