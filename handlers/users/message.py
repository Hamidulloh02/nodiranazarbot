from aiogram import types
from aiogram.dispatcher import FSMContext
from states.States import States
from data.config import ADMINS
from loader import dp, bot
from keyboards.inline.buttons import *

#  text = f'{message.from_user.get_mention()}\n@{message.from_user.username}\n\n{message.html_text}', 

@dp.message_handler(state=None, content_types = types.ContentTypes.ANY)
async def bot_echo(message: types.Message):
    for admin in ADMINS:
        try:
            # Foydalanuvchi ma'lumotlari
            user_info = f'{message.from_user.get_mention()}\{message.from_user.id}\n{message.html_text}'

            # Xabarni administratorga yuborish
            await bot.send_message(
                chat_id=admin,
                text=user_info,
                reply_markup=await ReplyBtn(
                    user_id=message.from_user.id,
                    msg_id=message.message_id,
                    user_name=message.from_user.username
                )
            )

        except Exception as e:
            print(f"Xabar yuborishda xato yuz berdi: {str(e)}")

    await message.reply("Tez orada javob beriladi iltimos kuting")

@dp.callback_query_handler(text_contains='msg_answer')
async def msg_answer(call: types.CallbackQuery, state: FSMContext):
    data = call.data.rsplit(':')
    await state.update_data({'user_name':data[3],'user_id': data[1], 'msg_id' : data[2]})
    await call.message.reply(text='Javob xabaringizni yozing:')
    await States.ReplyText.set()
    

@dp.message_handler(state=States.ReplyText, content_types=types.ContentTypes.ANY)
async def reply_text(message: types.Message, state: FSMContext):
    data = await state.get_data()
    try:
        await bot.copy_message(
            chat_id = data.get('user_id'),
            from_chat_id = message.chat.id,
            message_id = message.message_id,
            reply_to_message_id = data.get('msg_id'),),


        
    except:
        pass
    
    await state.reset_state()
    