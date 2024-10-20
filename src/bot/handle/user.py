from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

import logging

from ..keyboards.reply import reply

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("Tg_bot")

router = Router()


class Art(StatesGroup):
    serial_title = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Здравствуйте {message.from_user.first_name}! 🖐🏻",
        reply_markup=reply
    )


@router.message(F.text == "Поиск сериала")
async def get_item_info(message: Message, state: FSMContext):
    logger.info('Handling get item info')
    await state.set_state(Art.serial_title)
    await message.answer(
        f"Введите название сериала, для поиска👇",
        reply_markup=reply,
    )


@router.message(Art.serial_title)
async def check_art(message: Message, state: FSMContext):
    await state.update_data(id=message.text)
    art = await state.get_data()
    await state.clear()
    logger.info(f"Got this serial title -->{art}")
