import csv
from BaseReader import BaseReader


class CSVReader(BaseReader):
    def load(self):
        try:
            with open(self.src, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                self.data = [row for row in reader]

        except FileNotFoundError:
            print(f"{self.src} not found")
            self.data = []


    def save(self):
        with open(self.dst, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(self.data)