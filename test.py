import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.bot.api import TelegramAPIServer
from aiogram.types import ContentType

API_TOKEN = '2051732171:AAE6SHQjqDipQLMQO9oqSJN_21ApjYD38R0'

logging.basicConfig(level=logging.INFO)

local_server = TelegramAPIServer.from_base('http://localhost')

bot = Bot(token=API_TOKEN, server=local_server)
dp = Dispatcher(bot)


@dp.message_handler(content_types=ContentType.ANY)
async def echo(message: types.Message):
    await message.copy_to(message.chat.id)


executor.start_polling(dp, skip_updates=True)