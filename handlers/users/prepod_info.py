from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.inline_switсh_language import *
from keyboards.inline.callback_datas import *
from filters.emoji import *
from parsing_data.parsing_main import *
from keyboards.default.menu import *
from keyboards.inline.subscribe_inline_button import *
from data.config import admins
from keyboards.default.menu import menu

@dp.message_handler(text=f'Получить данные о преподавателе')
async def prep(message:types.Message):
    await message.answer('Поиск преподавателя', reply_markup=menu)

@dp.callback_query_handler(prepod_callback.filter(fio = 'fioo'))
async def prepod(call:CallbackQuery):
    await call.message.answer(text ='Введите номер группы:')    
    

