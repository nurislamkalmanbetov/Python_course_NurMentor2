import requests

kluch = '2141dc73b32de4c517b3cb0064aa5372'
gorod = 'Bishkek' 

def get_url(kluch, gorod):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={gorod}&appid={kluch}&units=metric&lang=ru'
    response = requests.get(url).json()
    weather_description = response['weather'][0]['description']
    temperature = response['main']['temp']
    feels_like = response['main']['feels_like']
    humidity = response['main']['humidity']
    wind_speed = response['wind']['speed']

    weather_report = (
        f"Погода в {gorod}:\n"
        f"Описание: {weather_description.capitalize()}\n"
        f"Температура: {temperature}°C\n"
        f"Ощущается как: {feels_like}°C\n"
        f"Влажность: {humidity}%\n"
        f"Скорость ветра: {wind_speed} м/с\n"
    )
    return weather_report 

print(get_url('2141dc73b32de4c517b3cb0064aa5372', 'Bishkek'))