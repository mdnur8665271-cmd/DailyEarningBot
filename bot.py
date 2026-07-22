import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    
    await message.answer("🎉 Welcome to Daily Earning Bot!")

@dp.message(Command("ads"))
async def ads(message: Message):
    user_balance = {}

@dp.message(Command("claim"))
async def claim(message: Message):
    user_id = message.from_user.id

    if user_id not in user_balance:
        user_balance[user_id] = 0

    reward = 10
    user_balance[user_id] += reward

    await message.answer(
        f"🎉 অভিনন্দন!\n"
        f"আপনি {reward} Coins পেয়েছেন.\n"
        f"💰 মোট Balance: {user_balance[user_id]} Coins"
    )
    @dp.message(Command("balance"))
async def balance(message: Message):
    user_id = message.from_user.id
    balance = user_balance.get(user_id, 0)

    await message.answer(f"💰 আপনার Balance: {balance} Coins")
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎥 Watch Ad",
                    url="https://omg10.com/4/11368110"
                )
            ]
        ]
    )

    await message.answer(
        "💰 Reward পেতে নিচের বাটনে ক্লিক করুন।",
        reply_markup=keyboard
    )

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
