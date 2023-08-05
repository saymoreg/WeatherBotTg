import requests
import datetime
from config import telegram_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=telegram_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['weather', 'start', 'poqoda', 'погода'])
async def start_command(message: types.Message):
    await message.reply("Hey there! Write the name of the city so i can give you detailed weather information!")


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Clear ☀",
        "Clouds": "Cloudy ☁",
        "Rain": "Rainy ☔",
        "Drizzle": "Light Rain ☔",
        "Thunderstorm": "Thunder ⚡",
        "Snow": "Snowy ❄",
        "Mist": "Misty 🌫"
    }
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
        data = r.json()

        if data["cod"] != 200:
            await message.reply(f"Error: {data['message']}")
            return

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        wd = code_to_smile.get(weather_description, "Look at the window... Smth is happening!")

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = sunset_timestamp - sunrise_timestamp

        await message.reply(f"--- {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ---\n"
                            f"The weather in the city: {city}\n"
                            f"Temperature: {cur_weather}°C {wd}\n"
                            f"Humidity: {humidity}%\n"
                            f"Pressure: {pressure}mm.Hg\n"
                            f"Wind: {wind}m/s\n"
                            f"Sunrise at: {sunrise_timestamp}\n"
                            f"Sunset at: {sunset_timestamp}\n"
                            f"Day length: {length_of_the_day}")

    except requests.exceptions.RequestException as ex:
        await message.reply("Error: Failed to connect to the OpenWeatherMap API...")
    except Exception as ex:
        await message.reply("Error:", ex)
        await message.reply("Check the name of the city...")


if __name__ == '__main__':
    executor.start_polling(dp)
