from loader import *
from aiogram.types import Message, InputFile, ContentType
from data.config import ADMINS
import aioschedule
import asyncio


@dp.message_handler(text='download', user_id=ADMINS)
async def download_handler(message: Message):
    try:
        await message.answer_document(
            document = InputFile(path_or_bytesio='data/main.db'),
        )
    except:
        await message.answer('Something went wrong with download database.')


async def download():
    try:
        await bot.send_document(
            chat_id = ADMINS[0],
            document = InputFile(path_or_bytesio='data/main.db')
        )
    except:
        pass


async def scheduler():
    aioschedule.every().day.at('00:00').do(download)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)