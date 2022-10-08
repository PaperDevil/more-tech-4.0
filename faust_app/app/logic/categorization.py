import json


class Categorizer:
    _map: dict = json.load(
        open('categories_map.json', 'r+')
    )

    @classmethod
    def get_categories(cls):
        return cls._map.keys()

    @classmethod
    def categorize(cls, word: str):
        results = []
        for key, v in cls._map.items():
            if word in v:
                results.append(key)
        return results
