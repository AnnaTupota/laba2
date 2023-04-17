from main import dp
from aiogram import executor
if __name__ == '__bottyperl__':
   executor.start_polling(dp, skip_updates=True)

#Параметр skip_updates=True позволяет пропустить накопившиеся входящие сообщения, если они нам не важны
#настроить получение сообщений от сервера в Telegram. Если этого не сделать, то мы не получим ответы бота.
#Реализовать получение новых сообщений можно с помощью поллинга.
#Он работает очень просто — метод start_polling опрашивает сервер, проверяя на нём обновления. Если они есть, то они приходят в Telegram.
