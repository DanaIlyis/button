from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp

from Keyboard.default import menu

@dp.message_handler(Command("start"))
async def show_menu(message:Message):
    await message.answer("Choose one", reply_markup=menu)

@dp.message_handler(Text(equals=["Paris", "Madrid", "Stambul", "Seoul"]))
async def get_food(message:Message):
    await message.answer(f"Choosen {message.text}.Thanks",
                         reply_markup=ReplyKeyboardRemove())