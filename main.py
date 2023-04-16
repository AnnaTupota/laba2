import requests
import io
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
TOKEN = "6080032473:AAEUUDw0cB_r8ppZ0I28-o7x_mH44jkUIDs"
bot = Bot(token=TOKEN)#создадим экземпляр класса Bot, передав ему в качестве аргумента наш токен
dp = Dispatcher(bot)#экземпляр класса Dispatcher (dp), который в качестве аргумента получит bot

@dp.message_handler(commands=['start'])
#Декоратор — это «обёртка» вокруг функций, позволяющая влиять на их работу без изменения кода самих функций. В нашем случае мы управляем функцией, считая команды пользователя;
#commands=['start'] — это команда, которая связана с декоратором и запускает вложенную в него функцию;
    #message_handler — это декоратор, который реагирует на входящие сообщения и содержит в себе функцию ответа.
    # async def with_puree4 — создаёт асинхронную функцию, которая принимает в себя сообщение пользователя message, определяемое через тип Message.
async def send_motivation(message: types.Message):
    await message.reply("Привет! На связи жемчужинка милашка-мотивашка)\n  ")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #ReplyKeyboardMarkup — это шаблоны сообщений.
    buttons = ["кидай мотивашку", "хочу поболтать"]
    keyboard.add(*buttons)#добавили кнопки
        # await message.reply — определяет ответ пользователя, используя await из-за асинхронности работы библиотеки.
    await message.answer("Чем я могу помочь?", reply_markup=keyboard)

@dp.message_handler(Text(equals="кидай мотивашку"))
async def with_puree1(message: types.Message):
    await message.reply("Отличный выбор!")
        # Ищем мотивационную картинку в сети интернет
            #response = requests.get('https://source.unsplash.com/random/1920x1080/?motivation')
    response = requests.get('https://source.unsplash.com/featured/?motivation')
        # Отправляем картинку пользователю
    photo = io.BytesIO(response.content)
    await bot.send_photo(message.chat.id, photo)

@dp.message_handler(lambda message: message.text == "хочу поболтать")
async def without_puree2(message: types.Message):
    await message.reply("Прекрасно)\n Меня создала Аня, милый прогер. ")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Я пользователь", "прекрасный препод Артемий Андреевич", "Вернуться"]
    keyboard.add(*buttons)
    await message.answer("А кто ты? РАССКАЖИ О СЕБЕ", reply_markup=keyboard)

@dp.message_handler(Text(equals="Я пользователь"))
async def with_puree3(message: types.Message):
    await message.reply("очень рада знакомству) многое о вас слышала)")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Пойдёт", "Прекрасно)", "С тобой пообщался, и мне стало лучше)", "Вернуться"]
    keyboard.add(*buttons)
    await message.answer("Как прошёл твой день? Устал наверняка(", reply_markup=keyboard)
#async def with_puree4 — создаёт асинхронную функцию, которая принимает в себя сообщение пользователя message, определяемое через тип Message.
@dp.message_handler(Text(equals="Пойдёт"))
async def with_puree4(message: types.Message):
        #await message.reply — определяет ответ пользователя, используя await из-за асинхронности работы библиотеки.
    await message.reply("это хорошо")
#Теперь создадим событие, которое будет обрабатывать введённое пользователем сообщение:
@dp.message_handler(Text(equals="Прекрасно)"))
async def with_puree5(message: types.Message):
    await message.reply("здорово)")

@dp.message_handler(Text(equals="С тобой пообщался, и мне стало лучше)"))
async def with_puree6(message: types.Message):
    await message.reply("ура)")

@dp.message_handler(Text(equals="прекрасный препод Артемий Андреевич"))
async def with_pure7e(message: types.Message):
    await message.reply("извините, временные неполадки, надо чутка код починить...")

@dp.message_handler(lambda message: message.text == "Вернуться")
async def without_puree8(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["кидай мотивашку", "хочу поболтать"]
    keyboard.add(*buttons)
    await message.answer("Чем я могу помочь?", reply_markup=keyboard)

#настроить получение сообщений от сервера в Telegram. Если этого не сделать, то мы не получим ответы бота.
#Реализовать получение новых сообщений можно с помощью поллинга.
#Он работает очень просто — метод start_polling опрашивает сервер, проверяя на нём обновления. Если они есть, то они приходят в Telegram.
