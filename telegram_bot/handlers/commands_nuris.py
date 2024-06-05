from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


router = Router()


@router.message(CommandStart())
async def start(message:Message):
    description = (
        "Привет, я бот помощник! \n"
        "Этот бот предназначен для помощи \n"
        "Используй кнопки! \n"
        "/help \n"
        "/about \n" 
        "/weather_in_bishkek \n"
    )
    kb = [
        [KeyboardButton(text="/help")],
        [KeyboardButton(text="/about")],
        [KeyboardButton(text="hello")],
        [KeyboardButton(text="/weather_in_bishkek")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
    await message.answer(description, reply_markup=keyboard)




@router.message(Command(commands=['help']))
async def help(message:Message):
    await message.answer('For help call 911')

@router.message(Command(commands=['about']))
async def about_us(message:Message):
    await message.answer('We are awesome')

@router.message(F.text.lower() == 'hello')
async def hello(message:Message):
    await message.answer("Hello I'm bot ceo helper")

    


import requests 

API_KEY = '2141dc73b32de4c517b3cb0064aa5372'
CITY = 'Bishkek'

@router.message(Command(commands=['weather_in_bishkek']))
async def weather_in_bishkek(message: Message):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ru'
    response = requests.get(url).json()

    if response.get('cod') != 200:
        await message.answer("Не удалось получить данные о погоде.")
        return

    weather_description = response['weather'][0]['description']
    temperature = response['main']
    feels_like = response['main']
    humidity = response['main']
    wind_speed = response['wind']

    weather_report = (
        f"Погода в {CITY}:\n"
        f"Описание: {weather_description.capitalize()}\n"
        f"Температура: {temperature}°C\n"
        f"Ощущается как: {feels_like}°C\n"
        f"Влажность: {humidity}%\n"
        f"Скорость ветра: {wind_speed} м/с\n"
    )

    await message.answer(weather_report)


@router.message(F.text.lower() == 'привет')
async def hello(message: Message):
    await message.reply("Привет, я бот помощник SEO")