import sys
import os
from CSVreader import CSVReader
from JSONReader import JSONReader
from PickleReader import PickleReader

def get_reader(src, dst):
    ext = os.path.splitext(src)[1].lower()

    if ext == ".csv":
        return CSVReader(src, dst)
    elif ext == ".json":
        return JSONReader(src, dst)
    elif ext == ".pickle":
        return PickleReader(src, dst)
    else:
        print("Unsupported file format")
        sys.exit(1)


def main():

    if len(sys.argv) < 4:
        print("Usage: python reader.py <src> <dst> <change1> <change2> ...")
        sys.exit(1)

    src = sys.argv[1]
    dst = sys.argv[2]
    changes = sys.argv[3:]

    if not os.path.isfile(src):
        print(f"{src} does not exist")
        print("Available files:")
        for f in os.listdir("."):
            print(f)
        sys.exit(1)

    reader = get_reader(src, dst)
    reader.load()
    reader.changes(changes)
    reader.display()
    reader.save()


if __name__ == "__main__":
    main()