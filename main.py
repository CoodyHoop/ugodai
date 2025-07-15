from aiogram.client.default import DefaultBotProperties
import asyncio
from aiogram import Bot, Dispatcher
import logging
from dotenv import load_dotenv
import os



TOKEN = os.getenv("token")

from dotenv import load_dotenv
import os

print("Loading .env from:", os.path.abspath(".env"))
load_dotenv()
print("token after load_dotenv:", os.getenv("token"))

token = os.getenv("TOKEN")
print("token after explicit load_dotenv:", token)

import os
print(os.listdir()) 

from hrndlers.users.message import register_user_messages

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")

    bot = Bot(token, default=DefaultBotProperties(parse_mode='HTML'))  
    dp = Dispatcher()
    register_user_messages(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())