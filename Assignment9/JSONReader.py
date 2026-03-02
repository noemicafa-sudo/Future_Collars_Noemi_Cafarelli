import json
from BaseReader import BaseReader


class JSONReader(BaseReader):
    def load(self):
        try:
            with open(self.src, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            if not isinstance(self.data, list):
                self.data = []
        except FileNotFoundError:
            print(f"{self.src} not found")
            self.data = []
        except json.JSONDecodeError:
            self.data = []

    def save(self):
        with open(self.dst, "w", encoding='utf-8') as f:
            json.dump(self.data, f, indent=2)