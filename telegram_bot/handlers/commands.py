from aiogram import Router, F
from aiogram.filters import Command, CommandStart 
from aiogram.types import Message, CallbackQuery, FSInputFile

router = Router()


@router.message(CommandStart())
async def start(message:Message):
    await message.answer("Hello, i'm bot CEO helper")


@router.message(Command(commands=['help']))
async def help(message:Message):
    await message.answer("For help, please call to 999")


@router.message(Command(commands=['about']))
async def about_us(message:Message):
    await message.answer("Ne my ne kompaniya, my nayomnikix")


@router.message(F.text.lower() == 'hello')
async def hello(message:Message):
    await message.reply("Hello, i'm bot SEO helper")