from aiogram import Bot, Dispatcher, executor
import handlers
API_TOKEN = 'Very unsecure'
# создаем экземпляры бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# запускаем программу
dp.register_message_handler(handlers.start, commands=["start"])
dp.register_message_handler(handlers.echo)
if __name__ == '__main__':
# указание skip_updates=True
# пропустит команды,
# которые отправили
# до старта бота
    executor.start_polling(dp, skip_updates=True)

