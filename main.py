# import requests
# import datetime
# from pprint import pprint
# from config import open_weather_token
#
# THIS SECTION IS CREATED TO TEST THE CODE
#
# def get_weather(city, open_weather_token):
#     code_to_smile = {
#         "Clear": "Clear ☀",
#         "Clouds": "Cloudy ☁",
#         "Rain": "Rainy ☔",
#         "Drizzle": "Light Rain ☔",
#         "Thunderstorm": "Thunder ⚡",
#         "Snow": "Snowy ❄",
#         "Mist": "Misty 🌫"
#     }
#     try:
#         r = requests.get(
#             f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
#         data = r.json()
#
#         if data["cod"] != 200:
#             print(f"Error: {data['message']}")
#             return
#
#         city = data["name"]
#         cur_weather = data["main"]["temp"]
#
#         weather_description = data["weather"][0]["main"]
#         wd = code_to_smile.get(weather_description, "Look at the window... Smth is happening!")
#
#         humidity = data["main"]["humidity"]
#         pressure = data["main"]["pressure"]
#         wind = data["wind"]["speed"]
#         sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
#         sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
#         length_of_the_day = sunset_timestamp - sunrise_timestamp
#
#         print(f"--- {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ---")
#         print(f"The weather in the city: {city}")
#         print(f"Temperature: {cur_weather}°C {wd}")
#         print(f"Humidity: {humidity}%")
#         print(f"Pressure: {pressure}mm.Hg")
#         print(f"Wind: {wind}m/s")
#         print(f"Sunrise at: {sunrise_timestamp}")
#         print(f"Sunset at: {sunset_timestamp}")
#         print(f"Day length: {length_of_the_day}")
#
#     except requests.exceptions.RequestException as ex:
#         print("Error: Failed to connect to the OpenWeatherMap API...")
#     except Exception as ex:
#         print("Error:", ex)
#         print("Check the name of the city...")
#
#
# def main():
#     city = input("Enter the city name: ")
#     get_weather(city, open_weather_token)
#
#
# if __name__ == '__main__':
#     main()
