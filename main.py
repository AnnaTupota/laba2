import requests
import io
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
TOKEN = "6080032473:AAEUUDw0cB_r8ppZ0I28-o7x_mH44jkUIDs"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_motivation(message: types.Message):
    await message.reply("Привет! На связи жемчужинка милашка-мотивашка)\n  ")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["кидай мотивашку", "хочу поболтать"]
    keyboard.add(*buttons)
    await message.answer("Чем я могу помочь?", reply_markup=keyboard)

@dp.message_handler(Text(equals="кидай мотивашку"))
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!")
# Ищем мотивационную картинку в сети интернет
    response = requests.get('https://source.unsplash.com/featured/?motivation')
# Отправляем картинку пользователю
    photo = io.BytesIO(response.content)
    await bot.send_photo(message.chat.id, photo)

@dp.message_handler(lambda message: message.text == "хочу поболтать")
async def without_puree(message: types.Message):
    await message.reply("Прекрасно)\n Меня создала Аня, милый прогер. ")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Я пользователь", "прекрасный препод Артемий Андреевич"]
    keyboard.add(*buttons)
    await message.answer("А кто ты? РАССКАЖИ О СЕБЕ", reply_markup=keyboard)

@dp.message_handler(Text(equals="Я пользователь"))
async def with_puree(message: types.Message):
    await message.reply("очень рада знакомству) многое о вас слышала)")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Пойдёт", "Прекрасно)", "С тобой пообщался, и мне стало лучше)"]
    keyboard.add(*buttons)
    await message.answer("Как прошёл твой день? Устал наверняка(", reply_markup=keyboard)

@dp.message_handler(Text(equals="Пойдёт"))
async def with_puree(message: types.Message):
    await message.reply("это хорошо")

@dp.message_handler(Text(equals="Прекрасно)"))
async def with_puree(message: types.Message):
    await message.reply("здорово)")

@dp.message_handler(Text(equals="С тобой пообщался, и мне стало лучше)"))
async def with_puree(message: types.Message):
    await message.reply("ура)")

@dp.message_handler(Text(equals="прекрасный препод Артемий Андреевич"))
async def with_puree(message: types.Message):
    await message.reply("извините, временные неполадки, надо чутка код починить...")

