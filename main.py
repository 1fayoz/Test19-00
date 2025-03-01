from aiogram import Bot, Dispatcher, Router
import asyncio
from test import router as test_router



router = Router()
router.include_router(test_router)



async def main() -> None:
    bot = Bot(token="8052894221:AAFIZUdw4wT_jn6fTy56WTVn-JIjyTsURfo")
    dp = Dispatcher()

    dp.include_router(router)

    print("started")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
