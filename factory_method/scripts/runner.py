from .csv_extract import CsvDataExtractor
from .json_extract import JsonDataExtractor

def data_factory_extraction(file_path):
    if file_path.endswith(".csv"):
        extractor = CsvDataExtractor
    elif file_path.endswith(".json"):
        extractor = JsonDataExtractor
    else:
        raise TypeError("Invalid file type.")
    return extractor(file_path)

def extract_data_from(file_path):
    factory_object = None
    try:
        factory_object = data_factory_extraction(file_path)
    except Exception as e:
        print(e)
    return factory_object

if __name__ == '__main__':
    output_str = extract_data_from(r"C:\Users\jvasa\IdeaProjects\design_patterns\factory_method\source\input.json")
    print(output_str)






