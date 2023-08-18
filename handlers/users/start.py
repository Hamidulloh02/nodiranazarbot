import sqlite3
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.buttons import *
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.reset_state()
    if db.get_user(user_id=message.from_user.id):
        await message.answer(text='Assalomu alaykum')
    else:
        db.insert_user(
            user_id = message.from_user.id,
            full_name = message.from_user.full_name,
            username = message.from_user.username,
            status = 'user')
        await  message.answer(text='registered') 
    await bot.send_message()