from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def make_keyboard(back_index: int, next_index: int, list_len: int) -> InlineKeyboardMarkup:
    inline_keyboard = [
        [

        ],
        [
            InlineKeyboardButton(text="Подписаться", callback_data="submit"),
        ],
    ]

    if back_index <= 0:
        inline_keyboard[0].append(
            InlineKeyboardButton(text="Вперед", callback_data="move")
        )
    elif next_index >= list_len:
        inline_keyboard[1].append(
            InlineKeyboardButton(text="Назад", callback_data="back")
        )
    else:
        inline_keyboard[0].append(
            InlineKeyboardButton(text="Назад", callback_data="back")
        )
        inline_keyboard[0].append(
            InlineKeyboardButton(text="Вперед", callback_data="move")
        )
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
