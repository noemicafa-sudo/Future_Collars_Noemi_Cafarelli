import os
import requests

class WeatherForecast:
    def __init__(self, filename = "weather_results.txt"):
        self.filename = filename
        self._data = {}
        self._load_file()

    def _load_file(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, 'r') as f:
            for line in f:
                date, value = line.strip().split(',')
                self._data[date] = float(value)

    def __setitem__(self, date, value):
        self._data[date] = value

        with open(self.filename, "a") as f:
            f.write(f"{date},{value}\n")

    def __getitem__(self, date):
        return self._data.get(date)

    def __iter__(self):
        return iter(self._data)

    def items(self):
        for date, value in self._data.items():
            yield (date, value)

    def fetch_weather(self, date):
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude=42.459044&longitude=14.198918"
            f"&daily=precipitation_sum"
            f"&timezone=Europe%2FLondon"
            f"&start_date={date}&end_date={date}"
        )

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data["daily"]["precipitation_sum"][0]
        except Exception:
            return None
