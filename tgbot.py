import requests
import config
from config import tg_bot_token, open_weather_token
import telebot


bot = telebot.TeleBot(token=config.tg_bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot-Weather")

@bot.message_handler(content_types=['text'])
def weather(message):
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
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
        data = r.json()

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

        bot.send_message(message.chat.id, f"Weather in {city}: {wd}\nTemperature {temp}°C, feels like: {feels_like}°C\n"
                               f"Humidity: {humidity}%, Clouds: {clouds}%")
    except:
        bot.send_message(message.chat.id, "\U00002620 Check city name \U00002620")



if __name__ == '__main__':
    bot.polling(none_stop=True)
