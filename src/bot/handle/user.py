from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

import logging

from cache.orm import save_json_to_redis, get_json_from_redis
from ..keyboards.inline import make_keyboard
from ..keyboards.reply import reply
from ..messages.user_message import make_serial_preview
from ..service.tvmaze_service import get_serials_by_name

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("Tg_bot")

router = Router()


class Art(StatesGroup):
    id = State()


class Pagination(StatesGroup):
    current_page = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Здравствуйте {message.from_user.first_name}! 🖐🏻",
        reply_markup=reply
    )


@router.message(F.text == "Поиск сериала")
async def get_item_info(message: Message, state: FSMContext):
    logger.info('Handling get item info')
    await state.set_state(Art.id)
    await message.answer(
        f"Введите название сериала, для поиска👇",
        reply_markup=reply,
    )


@router.message(Art.id)
async def check_art(message: Message, state: FSMContext):
    await state.update_data(id=message.text)
    context = await state.get_data()
    await state.clear()
    serials_list = await get_serials_by_name(context['id'])
    await state.update_data(back_page=0)
    await state.update_data(next_page=1)
    await state.update_data(current_page=0)
    keyboard = await make_keyboard(0, 1, len(serials_list))
    await save_json_to_redis(str(message.chat.id), serials_list)
    message_text = make_serial_preview(serials_list[0])
    await message.answer(
        message_text,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )


@router.callback_query(lambda c: c.data == "move" or c.data == "back")
async def move_to_next_serial(call: CallbackQuery, state: FSMContext):
    context = await state.get_data()
    if call.data == "move":
        back_page = context['current_page'] + 1
        next_page = context['current_page'] + 2
    else:
        back_page = context['current_page'] - 1
        next_page = context['current_page']
    serials_list = await get_json_from_redis(str(call.message.chat.id))
    keyboard = await make_keyboard(back_page, next_page, len(serials_list))
    await state.update_data(next_page=next_page)
    await state.update_data(back_page=back_page)
    await state.update_data(current_page=back_page)
    message_text = make_serial_preview(serials_list[back_page])
    await call.message.edit_text(
        message_text,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )
