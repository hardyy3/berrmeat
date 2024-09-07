import asyncio
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

API_TOKEN = '7487011875:AAHXx7XwAG30P39UK6L_4rUll3KrAlPbO2s'  # Ваш токен бота

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

router = Router()


# Клавиатура с WebApp кнопкой
@router.message(Command("start"))
async def start(message: types.Message):
    keyboard = InlineKeyboardBuilder()
    web_app_url = "https://github.com/hardyy3/berrmeat.git"  # URL вашего веб-приложения
    web_app = types.WebAppInfo(url=web_app_url)

    # Добавляем кнопку, которая открывает WebApp
    keyboard.add(types.InlineKeyboardButton(text="Открыть меню", web_app=web_app))

    await message.answer("Добро пожаловать! Откройте меню:", reply_markup=keyboard.as_markup())


# Обработчик данных из WebApp
@router.message(Command("web_data"))
async def web_data_handler(message: types.Message, web_app_data: types.WebAppData):
    data = web_app_data.data  # Данные, переданные из WebApp
    await message.answer(f"Получены данные: {data}")


# Запуск бота
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
