from get_date import user_data, forecast
from api_request import fetch_weather
from file_data import read_from_file, save_to_file

def program():
    date = user_data()
    if date is None:
        return

    saved_value = read_from_file(date)
    if saved_value is not None:
        print("Result already in the file ")
        print(forecast(saved_value))
        return

    precipitation = fetch_weather(date)

    if precipitation is not None:
        save_to_file(date, precipitation)

    print(forecast(precipitation))

if __name__ == "__main__":
    program()

