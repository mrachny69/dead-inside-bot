from main import bot, dp

from aiogram.types import Message
from config import admin_id

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text='Я готова семпай <3')

@dp.message_handler()
async def echo(message: Message):
    await message.answer(text=message.text)