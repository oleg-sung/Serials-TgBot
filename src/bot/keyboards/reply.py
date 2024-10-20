from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Поиск сериала"),
        ],
        [
            KeyboardButton(text="Подкписки"),
        ],
    ],
    resize_keyboard=True,
)
