from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def send_welcome(message: types.Message):
    chat_id = message.chat.id
    await message.answer(text=f"Bu sizning ID: {chat_id}")
