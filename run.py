
import logging
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor



import sys
import logging

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters import CommandStart, Command
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message



bot = Bot(token='8117652130:AAE2pfxX_2ahWO3CiafUBxUSMUG_Dlv1rpw')
dp=Dispatcher(bot)





ALLOWED_USERS = {
                1630526670,
                911415411}  # Разрешенные ID пользователей

async def check_user_permissions(user_id):
    return user_id in ALLOWED_USERS

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = message.from_user.id
    if await check_user_permissions(user_id):
        await message.answer('Привет!✋\nДобро пожаловать в наше мини приложение!\n\n🖥Сайт-"Ссылка"\n\n👤Аккаунт тех.поддережки - @grishka_00\n\n🧷Инструкция по использованию приложенияn\n🧷Инструкция по использованию бота')
    else:
        await message.answer("У вас нет доступа к этому боту.")



@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    username = message.from_user.username or "Пользователь без имени"
    username_link = f"@{username}" if message.from_user.username else "Пользователь без имени"
    await bot.send_message(chat_id=1630526670, text=f"Пользователь с именем {username_link} хочет связаться с вами.")
    await message.answer("Спасибо за оставленную заявку, в скором времени мы с вами свяжемся.")



if __name__ == '__main__':
    try:
        executor.start_polling(dp)
    except KeyboardInterrupt:
        print('Бот выключен')
    

async def run():
    await dp.start_polling(bot)

