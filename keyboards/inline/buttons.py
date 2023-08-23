from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def ReplyBtn(user_id, msg_id,user_name):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.insert(InlineKeyboardButton(text='Javob berish', callback_data=f'msg_answer:{user_id}:{msg_id}:{user_name}'))
    return markup