import requests

latitude = 42.459044
longitude = 14.198918

def fetch_weather(date):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&daily=precipitation_sum"
        f"&timezone=Europe%2FLondon"
        f"&start_date={date}&end_date={date}"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        precipitation = weather_data["daily"]["precipitation_sum"][0]
        return precipitation
    except Exception as e:
        print ("Error finding data", e)
        return None