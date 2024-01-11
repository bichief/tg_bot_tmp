from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет!')