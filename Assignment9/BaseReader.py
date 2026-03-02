from abc import ABC, abstractmethod


class BaseReader(ABC):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.data = []

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self):
        pass

    def changes(self, changes):
        for change in changes:
            try:
                col_str, row_str, value = change.split(",", 2)
                col = int(col_str)
                row = int(row_str)

                while len(self.data) <= row:
                    self.data.append([])
                while len(self.data[row]) <= col:
                    self.data[row].append("")
                self.data[row][col] = value

            except ValueError:
                print(f"Invalid format: {change}")
            except Exception as e:
                print(f"Error applying change '{change}': {e}")

    def display(self):
        for row in self.data:
            print(",".join(str(cell) for cell in row))
