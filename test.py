import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.bot.api import TelegramAPIServer
from aiogram.types import ContentType

API_TOKEN = '5168841978:AAGVRD7RD1T5mhvmI99ZPFEXIsvQQb5kCh0'

logging.basicConfig(level=logging.INFO)

local_server = TelegramAPIServer.from_base('http://188.163.35.182')

bot = Bot(token=API_TOKEN, server=local_server)
dp = Dispatcher(bot)


@dp.message_handler(content_types=ContentType.ANY)
async def echo(message: types.Message):
    await message.copy_to(message.chat.id)


executor.start_polling(dp, skip_updates=True)
