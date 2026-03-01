from get_date import user_data, forecast
from Weatherclass import WeatherForecast

def program():

    weather_forecast = WeatherForecast()

    date = user_data()
    if not date:
        return

    if weather_forecast[date] is not None:
        print("Result already saved:")
        print(forecast(weather_forecast[date]))
    else:
        precipitation = weather_forecast.fetch_weather(date)
        if precipitation is not None:
            weather_forecast[date] = precipitation
        print(forecast(precipitation))

    print("\nSaved forecasts:")
    for date, value in weather_forecast.items():
        print(date, value)


if __name__ == "__main__":
    program()

