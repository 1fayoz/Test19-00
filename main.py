from aiogram import types, Bot, Dispatcher
from aiogram.filters import CommandStart 
import asyncio


bot = Bot(token="8052894221:AAFIZUdw4wT_jn6fTy56WTVn-JIjyTsURfo")
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    chat_id = message.chat.id

    await message.answer(text=f"Bu sizning ID: {chat_id}")


async def main() -> None:
    print("started")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
