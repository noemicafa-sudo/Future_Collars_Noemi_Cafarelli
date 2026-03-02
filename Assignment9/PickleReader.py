import pickle
from BaseReader import BaseReader


class PickleReader(BaseReader):
    def load(self):
        try:
            with open(self.src, "rb") as f:
                self.data = pickle.load(f)
                if not isinstance(self.data, list):
                    self.data = []

        except FileNotFoundError:
            print(f"{self.src} not found")
            self.data = []
        except Exception:
            self.data = []


    def save(self):
        with open(self.dst, "wb") as f:
            pickle.dump(self.data, f)