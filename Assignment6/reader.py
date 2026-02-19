import sys
import os
import csv

data = [
    ["door", 3,7,0],
    ["sand", 12,5,1],
    ["brush", 22,34,5],
    ["poster", "red", 8, "stick" ]
]
with open("in.csv", "w", newline = '') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("File created")

args = sys.argv
if len(args) < 3:
    print("Write the following: reader.py <src> <dst> <change1> <change2> ...")
    sys.exit(1)

src = args[1]
dst = args[2]
changes = args[3:]

if not os.path.isfile(src):
    print(f"{src} does not exist")
    print("Available files:")
    for f in os.listdir("."):
        print(f)
    sys.exit(1)

with open(src, newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

for change in changes:
    try:
        col_str, row_str, value = change.split(",", 2)
        col = int(col_str)
        row = int(row_str)

        if row < 0 or row >= len(data):
            print(f"Row {row} does not exist")
            continue
        if col < 0 or col >= len(data[row]):
            print(f"Column {col} does not exist")
            continue

        data[row][col] = value

    except ValueError:
        print(f"Format error: {change}")


for row in data:
    print(",".join(row))

with open(dst, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
