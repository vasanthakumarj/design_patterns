import json

class JsonDataExtractor():
    def __init__(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as finp:
            self.data = json.load(finp)

    @property
    def parsed_data(self):
        return self.data
