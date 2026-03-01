from datetime import datetime, timedelta

def user_data():
    while True:
        user_input = input("Please enter your date in the format YYYY-MM-DD: ")

        if user_input == "":
          tomorrow = datetime.today() + timedelta(days=1)
          return tomorrow.strftime("%Y-%m-%d")

        try:
            good_date = datetime.strptime(user_input, "%Y-%m-%d")
            return good_date.strftime("%Y-%m-%d")
        except ValueError:
            print ("Invalid date")

def forecast(value):
    if value is None or value < 0:
        return "I don't Know"
    elif value > 0.0:
        return f"It will rain. Precipitation: {value} mm"
    else:
        return "It will not rain"