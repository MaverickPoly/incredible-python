import requests
import pprint
import argparse
import dotenv
import os


dotenv.load_dotenv()
API_KEY = os.getenv("OPEN_WEATHER_MAP_API")
URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"


def main():
    parser = argparse.ArgumentParser(description="Weather App CLI")
    parser.add_argument("city", help="Target city fetch weather for.")
    args = parser.parse_args()
    url = URL.format(args.city, API_KEY)

    response = requests.get(url)
    if response.ok:
        json_data = response.json()
        # pprint.pprint(json_data)

        temperature = json_data["main"]["temp"]
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        city = json_data["name"]
        description = json_data["weather"][0]["description"]

        print(f"====== {city} ======")
        print(f"Temperature: {temperature} C")
        print(f"Air pressure: {pressure}")
        print(f"Humidity: {humidity}")
        print(f"Description: {description}")


if __name__ == '__main__':
    main()
