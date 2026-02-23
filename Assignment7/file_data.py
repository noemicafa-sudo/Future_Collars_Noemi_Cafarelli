import os

filename = "weather_results.txt"

def read_from_file(date):
    if not os.path.exists(filename):
        return None
    with open(filename, "r") as file:
        for line in file:
            saved_date, saved_value = line.strip().split(",")
            if saved_date == date:
                return float(saved_value)
    return None

def save_to_file(date, value):
    with open(filename, "a") as file:
        file.write(f"{date},{value}\n")
