from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Paris"),
            KeyboardButton(text="Madrid"),
        ],
        [
            KeyboardButton(text="Stambul"),
            KeyboardButton(text="Seoul"),
        ],
        [
            KeyboardButton(text="shymkent"),
            KeyboardButton(text="taraz"),
            KeyboardButton(text="almaty"),
        ],
    ],
    resize_keyboard=True
)

