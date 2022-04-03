import requests
from pprint import pprint
from config import open_weather_token

def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B"
    }

    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
        data = r.json()
        pprint(data)

        city = data["name"]
        temp = data["main"]["temp"]

        weather_desc = data["weather"][0]["main"]
        if weather_desc in code_to_smile:
            wd = code_to_smile[weather_desc]
        else:
            wd = "No info!"

        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        clouds = data["clouds"]["all"]

        print(f"Weather in: {city}: {wd}\nTemperature {temp}°C, feels like: {feels_like}°C\n"
              f"Humidity: {humidity}%, Clouds: {clouds}%")

    except Exception as ex:
        print(ex)
        print("Check city name!")


def main():
    city = input("Type your city: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()



