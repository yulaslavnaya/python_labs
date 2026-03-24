import requests

city = input("Введите название города: ").strip()

if not city:
    print("Название города не может быть пустым!")
    exit()

URL = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": "79d1ca96933b0328e1c7e3e7a26cb347",
    "units": "metric",
    "lang": "ru"
}

weather_data = requests.get(URL, params=params).json()

temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
wind_speed = round(weather_data['wind']['speed'])
pressure = round(weather_data['main']['pressure'])
humidity = round(weather_data['main']['humidity'])
weather_desc = weather_data["weather"][0]["description"]

print('Сейчас в городе', city, str(temperature), '°C')
print('Ощущается как', str(temperature_feels), '°C')
print('Ветер', str(wind_speed), 'м/с')
print('Давление', str(pressure), 'гПа')
print('Влажность', str(humidity), '%')
print(str(weather_desc))